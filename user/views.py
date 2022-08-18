from django.contrib import auth
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django import views
from . import forms, models
from django.utils.crypto import get_random_string
# Create your views here.

class SignInView(views.View):
    def get(self, request):
        form = forms.SignInForm()
        return render(request, 'user/signin.html', {'form': form})
    def post(self, request:HttpRequest):
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
            print('salam')
            return render(request, 'user/signup.html', {'form': form})
            data = form.cleaned_data
            new_user = models.User(
                first_name=data['first'],
                last_name=data['last'],
                email=data['email'],
                phone=data['phone'],
                username=data['email'],
                activation_code=get_random_string(length=128)
            )
            new_user.set_password(data['password'])
            new_user.save()
            form = forms.SignUpForm()
            return render(request, 'user/signup.html', {'form': form, 'success': True})
        return render(request, 'user/signup.html', {'form': form})

class RecoveryView(views.View):
    def get(self, request:HttpRequest):
        form = forms.PasswordRecoveryForm()
        return render(request, 'user/recovery.html', {'form': form})

    def post(self, request:HttpRequest):
            form = forms.PasswordRecoveryForm(request.POST)
            if form.is_valid():
                user = models.User.objects.filter(email=form.cleaned_data['email']).first()
                if user and user.phone == form.cleaned_data.get('phone'):
                    print(form.cleaned_data['captcha'])
                    pass # TODO: send email
                form = forms.PasswordRecoveryForm()
                return render(request, 'user/recovery.html', {'form': form, 'success': True})
            return render(request, 'user/recovery.html', {'form': form})

class DashboardView(views.View):
    def get(self, request):
        return render(request, 'user/dashboard.html')

class DashboardCoursesView(views.View):
    def get(self, request):
        return render(request, 'user/dashboard-courses.html')

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

class DashboardOnlineClassesView(views.View):
    def get(self, request):
        return render(request, 'user/dashboard-online-classes.html')

class DashboardCalenderView(views.View):
    def get(self, request):
        return render(request, 'user/dashboard-calender.html')

class DashboardSupportView(views.View):
    def get(self, request):
        return render(request, 'user/dashboard-support.html')

class UserProfileView(views.View):
    def get(self, request):
        return render(request, 'user/profile.html')

class UserPasswordResetRequestView(views.View):
    def get(self, request):
        return render(request, 'user/user-password-reset-request.html')

class UserPasswordResetView(views.View):
    def get(self, request, activation_code):
        if not request.user.activation_code == activation_code:
            return redirect('UserSignInURL')
        return render(request, 'user/user-password-reset-request.html')

def sign_out(request:HttpRequest):
    auth.logout(request)
    return redirect('HomeURL')