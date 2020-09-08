from django.urls import path
from .views import blog_view, post_view

urlpatterns = [
    path('blog/', blog_view, name='blog'),
    path('blog/<str:id>/', post_view, name='post')
]
