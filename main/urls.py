from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('list', views.bookmark_list_view, name="bookmark_list"),
    path('edit/<int:id>', views.edit_bookmark_view, name="edit_bookmark")
]