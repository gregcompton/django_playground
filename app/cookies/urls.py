from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'cookies'

urlpatterns = [
    path('', views.index, name="cookies"),
    path('set_cookie', views.setting_cookie, name='set_cookie'),
    path('get_cookie', views.getting_cookie, name='get_cookie'),
    path('update_cookie', views.updating_cookie, name='update_cookie'),
    path('update_cookie_redirect', views.redirect_update_cookie, name='redirect_update'),
    path('delete_cookie', views.deleting_cookie, name='delete_cookie'),
]
