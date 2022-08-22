from django.shortcuts import render
from django import views
from django.template.loader import render_to_string

from . import forms
from utils import mail


# Create your views here.

class SupportView(views.View):
    def get(self, request):
        form = forms.SupportTicketModelForm()
        return render(request, 'contact/support.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            QueryDict = request.POST.copy()
            QueryDict['email'] = request.user.email
            QueryDict['first_name'] = request.user.first_name
            QueryDict['last_name'] = request.user.last_name
            request.POST = QueryDict
        form = forms.SupportTicketModelForm(request.POST)
        if form.is_valid():
            form.save()
            mail.send_mail(to=form.cleaned_data['email'], fr='noreply@xtechno.ir',
                           subject='تیکت پشتیبانی',
                           text=render_to_string('email/email-activation.html'))
            form = forms.SupportTicketModelForm()
            return render(request, 'contact/support.html', {'form': form, 'success': True})
        else:
            return render(request, 'contact/support.html', {'form': form})


class AboutUsView(views.View):
    def get(self, request):
        return render(request, 'contact/about-us.html')


class ContactUsView(views.View):
    def get(self, request):
        form = forms.ContactMessageModelForm()
        return render(request, 'contact/contact-us.html', {'form': form, 'success': False})

    def post(self, request):
        form = forms.ContactMessageModelForm(request.POST)
        if form.is_valid():
            form = forms.ContactMessageModelForm()
            form.save()
            return render(request, 'contact/contact-us.html', {'form': form, 'success': True})
        return render(request, 'contact/contact-us.html', {'form': form, 'success': False})
