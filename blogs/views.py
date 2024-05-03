from django.shortcuts import render,redirect
from http.client import HTTPResponse
from blogs.models import  Blog,Category
# Create your views here.

def posts_by_category(request,category_id):
    posts = Blog.objects.filter(status='Published',category=category_id)
    #use try/except when we want to do some custom action if the category does not exits
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    #use get_object_or_404 when you want to show 404 eoor page if the category does not exit
    #category get_object_404(Category,pk=category_id)
    context= {
        'posts':posts,
        'category':category,
        }
    return render(request ,'Posts_by_category.html' ,context)