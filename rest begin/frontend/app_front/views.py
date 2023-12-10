from django.shortcuts import render, redirect
import requests

# Create your views here.
def list_users(request):
    response = requests.get('http://127.0.0.1:8000/')
    tasks = response.json()
    return render(request, 'list.html', {'tasks':tasks})