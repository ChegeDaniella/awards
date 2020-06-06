from django.shortcuts import render,redirect
from .models import Posts
from django.views.generic import ListView, DetailView, CreateView
def index(request):
    return render(request,'projects/index.html')

def posts(request):
    context = {
        'posts':Posts.objects.all()
    }    

    return render(request,'projects/post.html', context)

class PostListView(ListView):
    model = Posts
    template_name = 'projects/post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Posts

class PostCreateView(CreateView):
    model = Posts
    fields = ['title','description','image_page','link']  

    

 
     



