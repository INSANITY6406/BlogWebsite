from django.shortcuts import render,redirect
from .  import forms
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    print("hello")
    return render(request,"main/home.html")

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