from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def list(request):
    blogs = Blog.objects
    return render(request, 'list.html', { 'blogs' : blogs })

def home(request):
    return render(request, 'home.html')
    
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog': blog_detail})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('detail', str(blog.id))

def write(request):
    return render(request, 'write.html')