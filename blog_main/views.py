
from http.client import HTTPResponse
from django.shortcuts import render
from blogs.models import Category,Blog,About,FollowUs


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    #print(featured_posts)

    posts = Blog.objects.filter(is_featured=True,status='Published')

    about = About.objects.all()[0]
    
    social_links = FollowUs.objects.all()
    #print(social_links)
    context = {
        'categories':categories,
        'featured_posts':featured_posts,
         'posts':posts,
         'about':about,
         'social_links':social_links,
       
       }
    return render(request, 'home.html' ,context)

