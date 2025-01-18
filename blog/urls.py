from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('blogs/', blogs,name='blogs'),
    path('blog/<str:slug>/', blog_details, name='blog_details'),
    path('category_blogs/<str:slug>/', category_blogs, name='category_blogs'),
    path('add_reply/<int:blog_id>/<int:comment_id>/', add_reply, name='add_reply'),
    path('my_blogs/', my_blogs, name='my_blogs'),
    path('add_blog/', add_blog, name='add_blog'),
    path('update_blog/<str:slug>/', update_blog, name='update_blog'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    
]
