from django.urls import path
from .views import BlogView, PublicBlogView


urlpatterns = [
    path("blog/", BlogView.as_view()),
    path("publicblog/", PublicBlogView.as_view()),
]
