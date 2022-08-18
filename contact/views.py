from django.shortcuts import render
from django import views

# Create your views here.

class SupportView(views.View):
    def get(self, request):
        return render(request, 'contact/support.html')

class AboutUsView(views.View):
    def get(self, request):
        return render(request, 'contact/about-us.html')

class ContactUsView(views.View):
    def get(self, request):
        return render(request, 'contact/contact-us.html')
