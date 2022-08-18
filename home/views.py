from django.shortcuts import render
from django import views
from course import models as course_models


# Create your views here.

def header_partial_view(request):
    return render(request, 'header-com.html')


class HomeView(views.View):
    def get(self, request):
        updated_courses = course_models.Course.objects.all().order_by('-update_date')[:4]
        popular_courses = course_models.Course.objects.all().order_by('-students')[:4]
        return render(request, 'home/home.html', {
            'popular_courses': popular_courses,
            'updated_courses': updated_courses,
        })
