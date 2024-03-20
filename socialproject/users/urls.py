from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth import logout
urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.user_login,name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
    
     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'),name='password_reset'),
     path('register/', views.register,name='register'),
     
     path('edit/', views.edit,name='edit'),
     
    
]
