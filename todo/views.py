from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import TodoForm
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404
from .task import send_email
from datetime import date

def todo_email():
    day = Todo.objects.filter(deadline =  date.today())
    if day > datetime.timedelta(minutes=10):
        user = users__pk
        if user == users.pk:
            send_email.delay(username=User.username, mail_adress=User.email)


#def todo_email():
#    for to in Todo.objects.all():
#        if to.deadline > datetime.timedelta(minutes=10):
#            user = users__pk
#            if user == to.user.pk:
#                send_email.delay(username=User.username, mail_adress=User.email)


@login_required
def todo(request):
    context ={}
    context['todo'] = Todo.objects.filter(users__pk = request.user.pk)
    print(context)
    return render(request, 'index.html', context)

@login_required
def create_todo(request):
    context = {}
    form = TodoForm(request.POST or None)
    context['todos'] = Todo.objects.filter(users__pk = request.user.pk)
    if form.is_valid():
        form.save()
        return redirect('todo')
    context["form"] = form
    return render(request, 'add.html', context)

#@login_required
#def update_todo(request, pk):
#    context = {}
#    context['todoss'] = Todo.objects.filter(users = request.user.pk)
#    todos = Todo.objects.get(pk=pk)
#    form = TodoForm(request.POST or None, instance=todos)
#
#    if form.is_valid():
#        form.save()
#        return redirect('list_todos')
#
#    return render(request, 'edit.html', context)

@login_required
def update_todo(request, pk):
    instance = get_object_or_404(Todo, pk=pk)
    context = {}
    context['todos'] = Todo.objects.filter(users__pk = request.user.pk)
    form = TodoForm(request.POST or None, instance=instance)
    tod = Todo.objects.get(pk=pk)
    context['form'] = form

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/')
    
    return render(request, 'edit.html', context)



    
@login_required
def del_todo(request, pk):
    context = {}
    context['to'] = Todo.objects.filter(users = request.user.pk)
    tod = Todo.objects.get(pk=pk)
    tod.delete()
    return redirect('todo')

@login_required
def todo_status(request, pk):
    context = {}
    context['to'] = Todo.objects.filter(users=request.user.pk)
    tod = Todo.objects.get(pk=pk)
    tod.status = False
    tod.save()
    return redirect('todo')

        

#class Todos(LoginRequiredMixin, ListView):
#    model = Todo
#    login_url = reverse_lazy('login')
#    template_name = 'index.html'
#
#    def get_queryset(self):
#        qs = super().get_queryset()
#
#        qs = qs.filter(User=self.request.user).order_by('name')
#
#        return qs
#
#class create_todo(LoginRequiredMixin, CreateView):
#    model = Todo
#    template_name = 'create_todo.html'
#    fields = ('name',)
#    success_url = reverse_lazy('Todos')
#    login_url = reverse_lazy('login')
#
#    def get_context_data(self, **kwargs):
#        context = super(LoginRequiredMixin, self).get_context_data(**kwargs)
#        context['users_fullname'] = f"{self.request.user.first_name} {self.request.user.last_name}"
#        return context
#
#    def form_valid(self, form):
#        form.instance.user = User.objects.get(pk=self.request.user.pk)
#        return super(LoginRequiredMixin, self).form_valid(form)
#
#class remove_todo(LoginRequiredMixin, DeleteView):
#    model = Product
#    template_name = 'remove_todo.html'
#    login_url = reverse_lazy('login')
#    success_url = reverse_lazy('Todos')
#
#class UpdateTodo(LoginRequiredMixin, UpdateView):
#    model = Product
#    template_name = 'update_product.html'
#    login_url = reverse_lazy('login')
#    success_url = reverse_lazy('Todos')
#    form_class = TodoForm
#
#    def get_form_kwargs(self):
#        kwargs = super(LoginRequiredMixin, self).get_form_kwargs()
#        kwargs['user'] = self.request.user
#        return kwargs
#
#def emailView(request):
#    if request.method == 'GET':
#        form = ContactForm()
#    else:
#        form = ContactForm(request.POST or None)
#        if form.is_valid():
#            subject = form.cleaned_data['subject']
#            from_email = form.cleaned_data['from_email']
#            message = form.cleaned_data['message']
#            try:
#                send_mail(subject, message, from_email, ['gulnarnecefova1996@gmail.com'])
#            except BadHeaderError:
#                return HttpResponse('Invalid header found.')
#            return redirect('success')
#    return render(request, "email.html", {'form': form})