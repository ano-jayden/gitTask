from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('skills/', views.skills_list, name='skills_list'), 
]
