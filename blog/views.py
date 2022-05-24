from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from .models import Post, Comment
from .forms import CommentForm

def index(request):
    latest_post_list = Post.objects.order_by('date')[:5]
    template = loader.get_template('blog/blog.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    template = loader.get_template('blog/details.html')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.date = timezone.now()
            comment.save()
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    
    return HttpResponse(template.render(context, request))