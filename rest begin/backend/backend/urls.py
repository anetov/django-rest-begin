from django.contrib import admin
from django.urls import path
from app.views import list_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_tasks)
]
