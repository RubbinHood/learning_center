from django.urls import path
from . import views


urlpatterns = [
    path('', views.CourseIndexView.as_view(), name='CourseIndexURL'),
    path('reg/<int:id>', views.CourseRegisterView.as_view(), name='CourseRegisterURL'),
    path('<int:id>', views.CourseSingleView.as_view(), name='CourseSingleURL'),
]