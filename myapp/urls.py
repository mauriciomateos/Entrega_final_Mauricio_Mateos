from django.urls import path
from django.contrib.auth import views as auth_views
from myapp.views import home, about, register, blog_detail, blog_list, blog_create, blog_edit, blog_delete, message_create, message_delete, message_list

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blogs/', blog_list, name='blog_list'),
    path('blog_create/', blog_create, name='blog_create'),
    path('blogs_edit/<int:blog_id>/', blog_edit, name='blog_edit'),
    path('blogs_delete/<int:blog_id>/', blog_delete, name='blog_delete'),
    path('message/', message_list, name='message_list'),
    path('message_create/', message_create, name='message_create'),
    path('message_delete/<int:message_id>/', message_delete, name='message_delete'),
]
