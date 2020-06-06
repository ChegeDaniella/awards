from django.shortcuts import render,redirect
from .models import Posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostsSerializer


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

class PostCreateView( LoginRequiredMixin,CreateView):
    model = Posts
    fields = ['title','description','image_page','link']  

    def form_valid(self, form):
        form.instance.designer = self.request.user
        return super().form_valid(form)

class PostUpdateView( UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Posts
    fields = ['title','description','image_page','link']  

    def form_valid(self, form):
        form.instance.designer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.designer:
            return True
        return False

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Posts      
    success_url='/posts'  
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.designer:
            return True
        return False

class PostsList(APIView):
    def get(self, request, format=None):
        all_posts = Posts.objects.all()
        serlializer = PostsSerializer(all_posts, many=True)
        return Response(serlializer.data)        

    

 
     



