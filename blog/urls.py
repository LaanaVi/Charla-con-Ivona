from django.urls import path
from .views import blog_view, post_view

from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap

sitemaps = {
    'posts': BlogSitemap()
}

urlpatterns = [
    path('blog/', blog_view, name='blog'),
    path('blog/<str:id>/', post_view, name='post'),
    path('sitemap.xml', sitemap,
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
