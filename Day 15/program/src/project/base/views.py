from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class PendingList(ListView):
    model = Task
    context_object_name = 'tasks'


class DetailTask(DetailView):
    model = Task
    context_object_name = 'task'
    # in case change the name of template
    # template_name = 'base/task.html'

