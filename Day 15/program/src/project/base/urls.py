from django.urls import path
from .views import PendingList, DetailTask

urlpatterns = [path('', PendingList.as_view(), name='pendings'),
               path('task/<int:pk>', DetailTask.as_view(), name='task')]
