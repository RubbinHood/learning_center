from django.db import models

from user import models as user_models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/courses')
    teacher = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    update_date = models.DateTimeField()
    students = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True) #TODO remove balnk null
    is_active = models.BooleanField(default=False)

class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_introduction = models.BooleanField(default=False)

class CourseSession(models.Model):
    section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

class CourceSessionContent(models.Model):
    session = models.ForeignKey(CourseSession, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_video = models.BooleanField(default=False)
    file = models.FileField(upload_to='content/courses')

class CourceRegistration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)
