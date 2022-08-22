from django import forms
from captcha import fields, widgets

from . import models


class ContactMessageModelForm(forms.ModelForm):
    captcha = fields.ReCaptchaField(widget=widgets.ReCaptchaV2Checkbox,
                                    private_key='6LfSVJwhAAAAACMAAr2jQlomUDc0oJcJcvVDGXZL',
                                    public_key='6LfSVJwhAAAAAIO8J9jPfYOXuZL3xhgOI-ihZeCY', label='من ربات نیستم')

    class Meta:
        model = models.ContactMessage
        fields = ['first_name', 'last_name', 'email', 'title', 'text', 'attachment']
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
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'attachment': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }


class SupportTicketModelForm(forms.ModelForm):
    captcha = fields.ReCaptchaField(widget=widgets.ReCaptchaV2Checkbox,
                                    private_key='6LfSVJwhAAAAACMAAr2jQlomUDc0oJcJcvVDGXZL',
                                    public_key='6LfSVJwhAAAAAIO8J9jPfYOXuZL3xhgOI-ihZeCY', label='من ربات نیستم')

    class Meta:
        model = models.SupportTicket
        fields = ['first_name', 'last_name', 'email', 'title', 'text', 'attachment']
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
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'attachment': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }
