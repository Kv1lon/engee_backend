from django.urls import path

from .views import Profile, ProfileUpdate, AddObj, RemoveObj

urlpatterns = [

    path('<slug:slug>/', Profile.as_view(), name='profile'),
    path('<slug:slug>/add', AddObj.as_view(), name='add_obj'),
    path('<slug:slug>/remove', RemoveObj.as_view(), name='remove_obj'),
    path('profile_edit/<slug:slug>/', ProfileUpdate.as_view(), name='profile_edit'),

]

