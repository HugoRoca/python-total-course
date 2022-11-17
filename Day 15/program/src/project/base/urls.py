from django.urls import path
from .views import PendingList

urlpatterns = [path('', PendingList.as_view(), name='pendings')]
