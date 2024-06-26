from unicodedata import category
from django.contrib import admin

from blogs.models import Category,Blog ,About,FollowUs,Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('title',)}
    list_display = ('title', 'category', 'author','status', 'is_featured')
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)
    

admin.site.register(Category)
admin.site.register(Blog ,BlogAdmin )
admin.site.register(About)
admin.site.register(FollowUs)
admin.site.register(Comment)

