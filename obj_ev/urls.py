from django.urls import path

from .views import ProfileObjEv, ObjEvDetail, ObjEvCreate

urlpatterns = [

    path('obj_ev/<slug:slug>', ProfileObjEv.as_view(), name='obj_ev_profile'),
    path('obj_ev', ObjEvDetail.as_view(), name='obj_ev'),
    path('obj_ev/create', ObjEvCreate.as_view(), name='obj_ev'),


]

