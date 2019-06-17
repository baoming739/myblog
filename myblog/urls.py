"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
import xadmin
from django.views.static import serve
from .settings import STATIC_ROOT,MEDIA_ROOT
from article.views import HomeView,TagsView,ArticleView,ArticleDetialView,TagsDetialView

urlpatterns = [
    url(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^$', HomeView.as_view(),name="home"),
    url(r'^tags/$', TagsView.as_view(),name="tags"),
    url(r'^article/$', ArticleView.as_view(),name="article"),
    url(r'^article/(?P<article_id>\d+)/', ArticleDetialView.as_view(),name="article_detail"),
    url(r'^tags/(?P<tags_id>.*)/', TagsDetialView.as_view(),name="tags_detail"),

]
