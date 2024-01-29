from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('home-two/', home_two, name="home_two"),
    path('home-three/', home_three, name="home_three"),
    path('blog-details/', blog_details, name="blog_details"),
    

]