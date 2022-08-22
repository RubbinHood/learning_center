from django.urls import path
from . import views
urlpatterns = [
    path('', views.ArticleIndexView.as_view(), name='ArticleIndexURL'),
    path('<slug:slug>', views.ArticleSingleView.as_view(), name='ArticleSingleURL'),
]