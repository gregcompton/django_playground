from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "app"

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('cookie/', include('cookies.urls')),
]
