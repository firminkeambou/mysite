from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):

    #form = UserCreationForm()
    if request.method == 'POST':
      # form = UserCreationForm(request.POST) ( very basic form without any modification)
        form = RegisterForm(request.POST)  # new form with modifications

        if form.is_valid(): # is_valid() controls as well unicity
           form.save()
           username=form.cleaned_data.get('username')
           messages.success(request,f'Welcome {username} , your account is successfully created,  just login down below')
           
           #return redirect('food:index')
           return redirect('login')  #login here is the name of the path from app (urls file)# messages is available to login template, because messages got created from this view
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form })


@login_required  # decorator that restricts access to profilepage view, which means, if you are not login, trying accessing this page will throw an error on the web browser, by default django will try to redirect us to the login page http://127.0.0.1:8000/accounts/login
def profilepage(request):
    return render(request,'users/profile.html')