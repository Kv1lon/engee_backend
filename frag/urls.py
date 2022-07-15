
from django.contrib import admin
from django.urls import path, include, re_path

from users.views import UserActivationView, ResetPasswordView
from . import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [

    path('api/v1/', include('stats.urls')),
    path('api/v1/', include('obj_ev.urls')),
    path('api/v1/', include('contacts.urls')),
    path('api/v1/', include('users.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
    path('password/reset/confirm/<str:uid>/<str:token>', ResetPasswordView.as_view()),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
