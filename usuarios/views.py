from django.shortcuts import render
from django.contrib.auth import authenticate , login
# Create your views here.

def login_view(request):
    return render(request, 'Login_v1/index.html')