from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='img/user', default='img/user/user.jpg')
    phone = models.CharField(max_length=10, blank=False, null=False, verbose_name='تلفن تماس')
    activation_code = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
