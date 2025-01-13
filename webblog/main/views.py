from django.shortcuts import render,redirect
from .  import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post

# Create your views here.
@login_required(login_url="/login")
def home(request):
    posts=Post.objects.all()
    if request.method=="POST":
        postid=request.POST.get("post-id")
        print("THE ID is ",postid)
        userid=request.POST.get("userid")
        # post=Post.objects.get(id=postid)
        if postid:
            post=Post.objects.get(id=postid)

            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):

                post.delete()
        elif userid:
            print("the id is"+userid)
            post=Post.objects.get(id=userid)

            user=User.objects.get(username=post.author)
            name=user.username
            if user and request.user.is_staff:
                try:
                    group=Group.objects.get(name="default")
                    group.user_set.remove(user)
                    post.delete()
                except:
                    pass
                try:
                    group=Group.objects.get(name="mod")
                    group.user_set.remove(user)
                    post.delete()
                except:
                    pass
                print("User Removed"+name)
                return redirect("/home")
        else:
            print("userid not found")
        
        
    return render(request,"main/home.html",{"posts":posts})

@login_required(login_url="/login")
@permission_required("main.add_post",login_url="/login",raise_exception=True)
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