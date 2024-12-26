from django.urls import path
from . import views 
urlpatterns = [
    path("Allcourses/",views.AllCourses),
    path("",views.AppHome),
    path("AllResource/",views.AllResource),
]
