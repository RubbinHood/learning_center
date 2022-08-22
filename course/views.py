from django.core import paginator
from django.db.models import Q
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


class CourseIndexView(views.View):
    def get(self, request):
        tag = request.GET.get('tag')
        search = request.GET.get('search')
        queryset = models.Course.objects.filter(is_active=True)
        if tag:
            if tag == 'free':
                queryset = queryset.filter(price=0)
            elif tag == 'paid':
                queryset = queryset.filter(price__igt=0)
            else:
                pass
        if search:
            queryset = queryset.filter(
                Q(title__contains=search) | Q(description__contains=search) | Q(text__contains=search))
        paginator_obj = paginator.Paginator(queryset, 6)
        page_obj = paginator_obj.get_page(request.GET.get('page'))
        if queryset:
            return render(request, 'course/course-index.html',
                          {'courses': page_obj, 'filtered_category': tag, 'search': search, 'not_found': False})
        else:
            return render(request, 'course/course-index.html',
                          {'couses': page_obj, 'filtered_category': tag, 'search': search, 'not_found': True})


class CourseSingleView(views.View):
    def get(self, request, id):
        course = models.Course.objects.filter(pk=id).first()
        if course:
            return render(request, 'course/course-single.html', {'course': course})
        else:
            raise Http404


class CourseRegisterView(views.View):
    def get(self, request, slug):
        return render(request, 'course/course-register.html')


def course_card_partial_view(request, course):
    return render(request, 'course/course-card-com.html', {'course': course})
