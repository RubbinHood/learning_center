from django.shortcuts import render
from django import views
from course import models as course_models
from article import models as article_models
from . import models

# Create your views here.

def header_partial_view(request):
    return render(request, 'header-com.html')


class HomeView(views.View):
    def get(self, request):
        banners = models.Banner.objects.filter(template__contains='home.html')
        updated_courses = course_models.Course.objects.all().order_by('-update_date')[:4]
        popular_courses = course_models.Course.objects.all().order_by('-students')[:4]
        latest_articles = article_models.Article.objects.filter(is_active=True).order_by('-date')[:4]
        return render(request, 'home/home.html', {
            'popular_courses': popular_courses,
            'updated_courses': updated_courses,
            'latest_articles': latest_articles,
            'banner1': banners[0],
            'banner2': banners[1],
        })
