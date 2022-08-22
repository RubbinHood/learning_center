from django.db import models
from user import models as user_models


# Create your models here.

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=300, verbose_name='نام')
    last_name = models.CharField(max_length=300, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='پست الکترونیکی')
    title = models.CharField(max_length=300, verbose_name='عنوان پیام')
    text = models.TextField(verbose_name='متن پیام')
    attachment = models.FileField(upload_to='contact', verbose_name='فایل ضمیمه', null=True, blank=True)


class SupportTicket(models.Model):
    first_name = models.CharField(max_length=300, verbose_name='نام')
    last_name = models.CharField(max_length=300, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='پست الکترونیکی')
    user = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name='عنوان پیام')
    text = models.TextField(verbose_name='متن پیام')
    attachment = models.FileField(upload_to='contact', verbose_name='فایل ضمیمه', null=True, blank=True)
