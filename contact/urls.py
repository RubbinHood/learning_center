from django.urls import path
from . import views

urlpatterns = [
    path('support', views.SupportView.as_view(), name='SupportURL'),
    path('about-us', views.AboutUsView.as_view(), name='AboutUsURL'),
    path('contact-us', views.ContactUsView.as_view(), name='ContactUsURL'),
]
