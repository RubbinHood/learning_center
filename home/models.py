from django.db import models

# Create your models here.

class HomeBannerModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/banner')
    link = models.URLField()
    is_active = models.BooleanField(default=False)