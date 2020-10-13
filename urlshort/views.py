from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout

def register(request):
    form = CreateUserform()
    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'urlshort/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(request,username = user, password = password)
        if my_user is not None:
            login(request,my_user)
            return redirect('home')
    return render(request,'urlshort/login.html')

def logoutPage(request):
    logout(request)
    return redirect('site')

def site(request):
    return render(request,'urlshort/site.html')

def home(request):
    return render(request,'urlshort/home.html')

def createblog(request):
    form = Blogform();
    frm = Blogform()
    if request.method == 'POST':
        form = Blogform(request.POST)
        frm = form.save(commit=False)
        frm.author = request.user
        frm.save()
        return redirect('home')
    context = {'form':form}
    return render(request,'urlshort/createblog.html',context)

def myblog(request):
    context = {'blog':Blog.objects.filter(author = request.user)}
    return render(request,'urlshort/myblog.html',context)
    
def createcomments(request,pk):
    post = get_object_or_404(Blog,pk = pk)
    form = Commentform()
    if request.method == 'POST':
        form = Commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.titlec = post
            comment.save()
            return redirect('myblog')
    context={'form':form}
    return render(request,'urlshort/createcomment.html',context)


def createreply(request,pk):
    comment = get_object_or_404(Comment,pk = pk)
    form = Replyform()
    if request.method == 'POST':
        form = Replyform(request.POST)
        frm = form.save(commit = False)
        frm.reptocomment = comment
        frm.save()
        return redirect('myblog')
    context={'form':form}
    return render(request,'urlshort/createreply.html',context)

def blogdetail(request,pk):
    post = get_object_or_404(Blog,pk = pk)
    comm = Comment.objects.filter(titlec = post)
    context = {'post':post,'comm':comm}
    return render(request,'urlshort/blogdetail.html',context)

def sendreply(request,pk):
    comm = get_object_or_404(Comment,pk = pk)
    rep = Replies.objects.filter(reptocomment = comm).order_by('-date')
    context={'rep':rep}
    return render(request,'urlshort/sendreply.html',context)


