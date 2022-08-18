from django.shortcuts import render
from django import views
from django.http import Http404

from . import models


# Create your views here.

class CourseIndexView(views.generic.ListView):
    template_name = 'course/course-index.html'
    model = models.Course
    paginate_by = 12
    context_object_name = 'courses'


class CourseSingleView(views.View):
    def get(self, request, id):
        course = models.Course.objects.filter(pk=id)
        if course:
            return render(request, 'course/course-single.html', {'course': course[0]})
        else:
            raise Http404

class CourseRegisterView(views.View):
    def get(self, request, slug):
        return render(request, 'course/course-register.html')


def course_card_partial_view(request, course):
    return render(request, 'course/course-card-com.html', {'course': course})
