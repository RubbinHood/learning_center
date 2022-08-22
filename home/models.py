from django.db import models


# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=100)
    template = models.CharField(max_length=300)


class BannerImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/banner')
    link = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    carousel = models.OneToOneField(Banner, on_delete=models.PROTECT)
