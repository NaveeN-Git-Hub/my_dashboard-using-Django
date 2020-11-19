from django.urls import path
from . import views

urlpatterns = [
   path('learn_html', views.learn_html, name='learn_html'),
   path('nnetwork_html', views.nnetwork_html, name='nnetwork_html'),
   path('blog_html', views.blog_html, name='blog_html'),
   path('learn_css', views.learn_css, name='learn_css'),
   path('view_css', views.view_css, name='view_css'),
   path('sample_webpage', views.sample_webpage, name='sample_webpage'),
]