from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from todo.models import Todo


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

    return render(request, 'login.html')

@login_required(login_url=reverse_lazy('login'))
def homepage(request):
    context ={}
    context['todo'] = Todo.objects.filter(users__pk = request.user.pk)
    print(context)
    return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
