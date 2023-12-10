
from django.contrib import admin
from django.urls import path
from app_front.views import list_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_users),
]
