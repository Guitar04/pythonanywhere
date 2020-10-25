from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as logins
from .models import Destination
from .models import *

from .form import *


def index(request):
    return render(request,'myweb/index.html')

def login(request):
    return render(request,'myweb/login.html')

def starter(request):
    return render(request,'myweb/starter.html')




def post(request):
    return render(request,'myweb/post.html')




def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            logins(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/sign_up.html',context)

def logout(req):
    logout_user(req)
    return redirect('login')





#--------DB----#
def legendary(req):
    Destinations = Destination.objects.all()
    return render(req, 'myweb/legendary.html', {'Destinations': Destinations})





