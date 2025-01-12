from django.shortcuts import render,redirect
from .  import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def home(request):
    print("hello")
    return render(request,"main/home.html")

@login_required(login_url="/login")
def create_post(request):
    if request.method=="POST":
        form=forms.PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user    
            post.save()
            return redirect("/home")
    else:
        form=forms.PostForm()
    return render(request,"main/create_post.html",{"form":form})

def signUp(request):
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            print(user)
            login(request,user)
            return redirect("/home")
    else:
        form=forms.RegistrationForm()
        
    return render(request,"registration/sign_up.html",{"form":form})