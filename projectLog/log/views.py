from turtle import title
from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts" : posts})

def new(request):
    if request.method == "POST":
        inputTitle = request.POST.get("title")
        inputBody = request.POST.get("body")
        
        newPost = Post(title=inputTitle,body=inputBody)
        newPost.save()
        return redirect("index")
        
    return render(request, "new.html")    
def delete(request, event_id):
    post = Post.objects.get(pk=event_id)
    post.delete()
    return redirect("index")    

def search(request):
    return render(request, "search.html")

def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,"post.html", {"post":post})