from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password'}))
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    class Meta:
        model = User
        fields = ('username', 'password', 'remember_me')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat the password'}))
    terms_of_service = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'terms_of_service')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-group col-md-6 mb-3', 'placeholder': 'Name'}), max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-group col-md-6 mb-3', 'placeholder': 'Email'}), max_length=150)
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class':  'mb-3', 'placeholder': 'Subject'}), max_length=250)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'mb-3', 'placeholder': 'Message'}), max_length=2000)
