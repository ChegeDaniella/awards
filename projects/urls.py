from . import views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from django.conf import settings
from .views import PostListView

urlpatterns = [
    url('^$',views.index, name="index"),
    url('^posts/',PostListView.as_view(), name="posts"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
