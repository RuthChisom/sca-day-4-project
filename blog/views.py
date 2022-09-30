from django.shortcuts import render, get_object_or_404
from .models import Post
# from django.http import Http404

# Create your views here.
def post_list(request): #displays the list of posts
    posts = Post.published.all()
    return render(request,
            'blog/post/list.html',
            {'posts': posts})

def post_detail(request, id):   #displays a single post
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    #the above is replaced by the get_object_or_404() shortcut
    post = get_object_or_404(Post,
                            id=id,
                            status=Post.Status.PUBLISHED)
    return render(request,
            'blog/post/detail.html',
            {'post': post})