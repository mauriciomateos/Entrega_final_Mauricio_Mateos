from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from myapp.models import  Page, Message
from myapp.forms import  PageForm, MessageForm

def home(request):
    blogs = Page.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def about(request):
    return render(request, 'about.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def blog_detail(request, blog_id):
    blog = Page.objects.get(id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


def blog_list(request):
    blogs = Page.objects.all()
    return render(request, 'blog_list.html', {'blog_entries': blogs})

@login_required
def blog_create(request):
    if request.method == 'POST':
        blog= Page()
        blog.author = request.user
        form = PageForm(request.POST,request.FILES,instance=blog)
        
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = PageForm()
    return render(request, 'blog_create.html', {'form': form, })

@login_required    
def blog_edit(request,blog_id):
    blog = Page.objects.get(id=blog_id)
    
    if request.method == 'POST' and blog.author == request.user:
        form = PageForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    return render(request, 'blog_edit.html', {'form': PageForm(instance=blog) })

@login_required
def blog_delete(request,blog_id):
    blog = Page.objects.get(id=blog_id)
    
    if request.method == 'POST' and blog.author == request.user:
        blog.delete()
    return redirect('blog_list')
    
@login_required
def message_list(request):
    objs = Message.objects.filter(user_to=request.user)
    return render(request, 'message_list.html', {'objs': objs })

@login_required
def message_create(request):
    if request.method == 'POST':
        obj= Message()
        obj.user_from = request.user
        form = MessageForm (request.POST,instance=obj)
        
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm ()
    return render(request, 'message_create.html', {'form': form, })


@login_required
def message_delete(request,message_id):
    obj = Message.objects.get(id=message_id)
    
    if request.method == 'POST' and obj.user_to == request.user:
        obj.delete()
    return redirect('message_list')
