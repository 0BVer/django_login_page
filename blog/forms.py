from django import forms

from blog.models import Users


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=32, required=True)
    password = forms.CharField(label='password', max_length=32, required=True)

    class Meta:
        model = Users
        fields = {
            'username',
            'password',
        }


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
