from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocufaLandingView.as_view(), name='DocufaLandingURL')
]