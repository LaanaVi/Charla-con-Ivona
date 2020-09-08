from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

def blog_view(request):
    posts = Post.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('-id')
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__icontains=query)
        ).distinct()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'posts': posts,
               'page_obj': page_obj
               }
    return render(request, 'blog/blog.html', context)


def post_view(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    return render(request, 'blog/post.html', context)
