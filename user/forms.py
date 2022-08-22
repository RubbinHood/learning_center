from django import forms
from captcha import fields, widgets

from . import models


class SignUpForm(forms.Form):
    first = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='نام')
    last = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='نام خانوادگی')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='پست الکترونیک')
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='شماره موبایل')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='کلمه عبور')
    password_rep = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='تکرار کلمه عبور')


class SignUpModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='کلمه عبور')
    password_rep = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='تکرار کلمه عبور')
    captcha = fields.ReCaptchaField(widget=widgets.ReCaptchaV2Checkbox,
                                    private_key='6LfKnYYhAAAAAG_dOlr_xi4pX1ZYD_SDyq5rIjGN', label='من ربات نیستم')

    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email', 'phone', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'tel',
            }),
            # 'password': forms.PasswordInput(attrs={
            #     'class': 'form-control'
            # }),
            # 'password_rep': forms.PasswordInput(attrs={
            #     'class': 'form-control'
            # }),
        }


class SignInForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput({'class': 'form-control'}))
    password = forms.CharField(label='گذرواژه', widget=forms.PasswordInput({'class': 'form-control'}))
    captcha = fields.ReCaptchaField(widget=widgets.ReCaptchaV2Checkbox,
                                    private_key='6LfKnYYhAAAAAG_dOlr_xi4pX1ZYD_SDyq5rIjGN', label='من ربات نیستم')


class PasswordRecoveryForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput({'class': 'form-control'}))
    phone = forms.CharField(label='تلفن تماس', widget=forms.TextInput({'class': 'form-control', 'type': 'tel'}))
    captcha = fields.ReCaptchaField(widget=widgets.ReCaptchaV2Checkbox,
                                    private_key='6LfKnYYhAAAAAG_dOlr_xi4pX1ZYD_SDyq5rIjGN', label='من ربات نیستم')


class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'phone', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'tel',
            }),
        }
