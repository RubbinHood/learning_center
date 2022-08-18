from django.shortcuts import render
from django import views


# Create your views here.

class ForumLandingView(views.View):
    def get(self, request):
        return render(request, 'forum/forum-landing.html')
