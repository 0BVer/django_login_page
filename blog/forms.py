from django import forms
from django.contrib.auth import authenticate, login
from django.db.models import CheckConstraint, Q

from blog.models import Users


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=32, required=True,
                               error_messages={'required': "please fill username"})
    password = forms.CharField(label='password', max_length=32, required=True,
                               error_messages={'required': "please fill password"})

    class Meta:
        model = Users
        fields = {
            'username',
            'password',
        }

    def clean(self):
        clean_data = super().clean()
        username = clean_data.get('username')
        password = clean_data.get('password')

        if username == '' or password == '':
            return False
        # CheckConstraint(check=Q(password__))


class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=32, required=True)
    password = forms.CharField(label='password', max_length=32, required=True)
    password_confirm = forms.CharField(label='password_confirm', max_length=32, required=True)
    email = forms.CharField(label='email', max_length=32, required=True)

    class Meta:
        model = Users
        fields = {
            'username',
            'password',
            'password_confirm',
            'email',
        }
