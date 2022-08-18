from django.shortcuts import render
from django import views

# Create your views here.

class ArticleIndexView(views.View):
    def get(self, request):
        return render(request, 'article/article-index.html')