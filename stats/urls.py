from django.urls import path

from .views import StatCreate, StatDelete,  StatList,StatDetail

urlpatterns = [

    path('create', StatCreate.as_view(), name='create'),
    path('delete/<slug:slug>', StatDelete.as_view(), name='delete'),
    path('list_stats', StatList.as_view(), name='list_stats'),



]

