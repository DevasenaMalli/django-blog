from django.shortcuts import render,redirect
from http.client import HTTPResponse 
from blogs.models import  Blog,Category,FollowUs
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.

def posts_by_category(request,category_id):
    posts = Blog.objects.filter(status='Published',category=category_id)
    #use try/except when we want to do some custom action if the category does not exits
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    #use get_object_or_404 when you want to show 404 eoor page if the category does not exit
    #category= get_object_or_404(Category,pk=category_id)
    context= {
        'posts':posts,
        'category':category,
        }
    return render(request ,'Posts_by_category.html' ,context)

def blogs(request,slug):
    single_blog = get_object_or_404(Blog,slug=slug,status='Published')
    social_links = FollowUs.objects.all()
    context = {
        'single_blog':single_blog,
        'social_links':social_links,
        }
    return render(request,'blogs.html',context)



def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword,status='Published') )
    context = {
        'blogs':blogs,
        'keyword': keyword,
        }
    return render(request,'search.html',context)