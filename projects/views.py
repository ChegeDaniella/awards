from django.shortcuts import render,redirect, get_object_or_404
from .models import Posts,Rates
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostsSerializer
from .forms import RateForm
from django.urls import reverse

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

def search_results(request):
    if 'titlPro' in request.GET and request.GET["titlPro"]:
        search_term = request.GET.get("titlPro")
        searched_proj = Posts.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html', {"message":message, "posts":searched_proj}) 

    else:
        message = "You have not searched anything.Please ensure you have searched"
        return render(request,'projects/search.html', {"message":message})

class RateCreateView(LoginRequiredMixin,CreateView):
    model = Rates
    fields = ['design_rate','usability_rate','content_rate']

    def dispatch(self, request, *args, **kwargs):
        self.Rates = get_object_or_404(Posts, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.post = self.Rates
        return super().form_invalid(form)

    def get_absolute_url(self):
        return reverse('', kwargs={'pk':self.pk})        


 
     



