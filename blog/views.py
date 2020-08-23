
from django.http import HttpResponse
from .models import Blog,Comment
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
# Create your views here.
def index(request):
    blog_latest_list = Blog.objects.all()
    context={ "blog_latest_list" : blog_latest_list }
    return render(request,'blog/index.html',context)

def detail(request,blog_id):
    blogcontent = get_object_or_404(Blog, pk=blog_id)
    order=blogcontent.comment_set.order_by('-co_date')
    context={'blogcontent':blogcontent,"order":order}
    return render(request, 'blog/detail.html',context ) #change

def comment(request,blog_id):
    blo=Blog.objects.get(pk=blog_id)
    context ={"blog_id":blog_id,"blo":blo}
    return render(request, 'blog/comment.html',context)

def ack(request,blog_id):
    p = Blog.objects.get(pk=blog_id)
    p.comment_set.create(put_comment=request.POST['comment'],co_date=timezone.now())
    return render(request, 'blog/ack.html',{"p":p})

def tweet(request):
    return render(request,'blog/tweet.html')

def about(request):
    return render(request,'blog/about.html')
