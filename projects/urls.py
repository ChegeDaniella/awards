from . import views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from django.conf import settings
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    url('^$',views.index, name="index"),
    url('^posts/',PostListView.as_view(), name="posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-Update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="new-post")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
