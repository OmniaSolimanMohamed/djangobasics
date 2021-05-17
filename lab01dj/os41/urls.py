from django.urls import path
from os41 import views
urlpatterns = [
    path('home/', views.home),
    path ('student/<st_id>',views.getstd),
    path('all', views.getallstds ),
    path ('new', views.newstd),
    path ('edit/<st_id>', views.editstudent),
    path ('delete/<st_id>', views.delstd),
]
