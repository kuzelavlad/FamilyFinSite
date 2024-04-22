from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError("This username is already taken.")
    return username


def validate_username(value):
    if not value.isalnum():
        raise ValidationError('Username can only contain letters and numbers.')


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', validators=[validate_username])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, min_length=8)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
