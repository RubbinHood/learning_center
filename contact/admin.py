from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.ContactMessage)
admin.site.register(models.SupportTicket)
