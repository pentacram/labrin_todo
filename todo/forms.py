from django import forms
from .models import Todo
from django.contrib.admin import widgets

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'starttime', 'deadline', 'users', 'status']
        widgets = {
            'starttime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),

        }





class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)