from django.urls import path

from .views import (
    HomePageView, 
    BlogDetailView, 
    BlogCreateView, 
    BlogEditView,
    BlogDeleteView
)

urlpatterns = [
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('blog/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
    path('blog/new/', BlogCreateView.as_view(), name='post_new'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]

