__author__ = 'aditya'
from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class meta:
        model = SignUp
        fields = ['email', 'fullname']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split["@"]
        domain, extension = provider.spli['.']
        if not domain == "USC":
            raise forms.ValidationError("Please make sure you use USC email")
        if not extension == "edu":
            raise forms.ValidationError("Please make sure you use edu extension")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name


