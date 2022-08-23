from django.contrib import auth
from django.contrib.auth import decorators
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django import views
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from utils import mail
from . import forms, models
from django.utils.crypto import get_random_string


# Create your views here.

class SignInView(views.View):
    def get(self, request):
        form = forms.SignInForm()
        return render(request, 'user/signin.html', {'form': form})

    def post(self, request: HttpRequest):
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            user = models.User.objects.filter(email=form.cleaned_data.get('email')).first()
            if user and user.check_password(form.cleaned_data.get('password')):
                auth.login(request, user)
                return redirect('HomeURL')
            else:
                form.add_error('email', 'ایمیل وارد شده با گذرواژه مطابقت ندارد.')
        return render(request, 'user/signin.html', {'form': form})


class SignUpView(views.View):
    def get(self, request):
        form = forms.SignUpModelForm()
        return render(request, 'user/signup.html', {'form': form})

    def post(self, request):
        form = forms.SignUpModelForm(request.POST)
        if form.is_valid():
            new_user = models.User(
                first_name=form.cleaned_data['first'],
                last_name=form.cleaned_data['last'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                username=form.cleaned_data['email'],
                activation_code=get_random_string(length=128)
            )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            new_user = models.User.objects.filter(email=new_user.email)
            mail.send_mail(to=form.cleaned_data['email'], fr='noreply@xtechno.ir',
                           subject='فعالسازی حساب کاربری',
                           text=render_to_string('email/email-activation.html', context={'user': new_user}))
            form = forms.SignUpForm()
            return render(request, 'user/signup.html', {'form': form, 'success': True})
        return render(request, 'user/signup.html', {'form': form})


class RecoveryView(views.View):
    def get(self, request: HttpRequest):
        form = forms.PasswordRecoveryForm()
        return render(request, 'user/recovery.html', {'form': form})

    def post(self, request: HttpRequest):
        form = forms.PasswordRecoveryForm(request.POST)
        if form.is_valid():
            user = models.User.objects.filter(email=form.cleaned_data['email']).first()
            if user and user.phone == form.cleaned_data.get('phone'):
                mail.send_mail(to=form.cleaned_data['email'], fr='noreply@xtechno.ir',
                               subject='درخواست تغییر کلمه عبور',
                               text=render_to_string('email/account-recovery.html'))
            form = forms.PasswordRecoveryForm()
            return render(request, 'user/recovery.html', {'form': form, 'success': True})
        return render(request, 'user/recovery.html', {'form': form})


@method_decorator(name='dispatch', decorator=login_required)
class DashboardView(views.View):
    def get(self, request):
        logged_in_user = request.user
        return render(request, 'user/dashboard.html', {'user': logged_in_user})


@method_decorator(name='dispatch', decorator=login_required)
class DashboardCoursesView(views.View):
    def get(self, request):
        return render(request, 'user/dashboard-courses.html')


@method_decorator(name='dispatch', decorator=login_required)
class DashboardProfileView(views.View):
    def get(self, request):
        logged_in_user = request.user
        form = forms.UserProfileModelForm(instance=logged_in_user)
        return render(request, 'user/dashboard-profile.html', {'form': form, 'user': logged_in_user})

    def post(self, request):
        logged_in_user = request.user
        form = forms.UserProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UserDashboardProfileURL')
        return render(request, 'user/dashboard-profile.html', {'form': form, 'user': logged_in_user})


@method_decorator(name='dispatch', decorator=login_required)
class DashboardOnlineClassesView(views.View):
    def get(self, request):
        return render(request, 'user/dashboard-online-classes.html')


@method_decorator(name='dispatch', decorator=login_required)
class DashboardCalenderView(views.View):
    def get(self, request):
        return render(request, 'user/dashboard-calender.html')


@method_decorator(name='dispatch', decorator=login_required)
class DashboardSupportView(views.View):
    def get(self, request):
        logged_in_user = models.User.objects.filter(id=request.user.id).first()
        form = forms.UserSupportModelForm()
        return render(request, 'user/dashboard-support.html', {'user': logged_in_user, 'form': form, 'success': False})


@method_decorator(name='dispatch', decorator=login_required)
class UserProfileView(views.View):
    def get(self, request):
        return render(request, 'user/profile.html')


def sign_out(request: HttpRequest):
    auth.logout(request)
    return redirect('HomeURL')
