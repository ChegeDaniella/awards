from . import views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path,include
from django.conf import settings
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    url('^$',PostListView.as_view(), name="posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-Update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    # url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='projects')),
    path('post/new/', PostCreateView.as_view(), name="new-post"),
    path('api/posts/', views.PostsList.as_view()),
    url(r'^search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
