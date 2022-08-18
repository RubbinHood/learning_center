from django.shortcuts import render
from django import views
# Create your views here.

class DocufaLandingView(views.View):
    def get(self, request):
        return render(request, 'docufa/docufa-landing.html')