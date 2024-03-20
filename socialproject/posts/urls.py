from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('create/',views.post_create,name='create'),
    path('feed/',views.feed,name='feed'),
    path('like/',views.like_post,name='like'),
]

