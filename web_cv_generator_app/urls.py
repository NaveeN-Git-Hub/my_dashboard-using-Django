from django.urls import path
from . import views

urlpatterns = [
   path('profile', views.profile, name='profile'),
   path('<int:id>/',views.resume, name="resume"),
   path('profiles_list',views.profiles_list, name="profiles_list"),
]