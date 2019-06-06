from django.contrib import admin
from .models import *

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('task', 'starttime', 'deadline', 'status')



