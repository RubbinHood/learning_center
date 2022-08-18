from django.urls import path
from . import views

urlpatterns = [
    path('', views.ForumLandingView.as_view(), name='ForumLandingURL')
]