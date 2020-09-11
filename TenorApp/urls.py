from django.urls import path
from . import views
app_name='TenorApp'
urlpatterns=[
    path('',views.home,name='home'),
    path('listing/',views.listing,name='listing'), 
    path('upvote/<int:pk>/',views.upvote,name='upvote'),
    path('downvote/<int:pk>/',views.downvote,name='downvote'),
    

]