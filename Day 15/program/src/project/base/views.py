from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


class PendingList(ListView):
    model = Task
    conext_object_name = 'tasks'
