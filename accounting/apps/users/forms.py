from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class UserRegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Паролите не съвпадат .'
    }

    username = forms.CharField(label='Потребителско име', max_length=150,
                               help_text='Позволени са букви, цифри и следните знаци : "@" "." "+" "-" "_" ',
                               error_messages={
                                   'required': 'Потребител с това име съществува .'
                               })
    password1 = forms.CharField(label='Парола',
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
                                help_text='Паролата трябва да е минимум 8 знака, нечесто срещана и различна от '
                                          'потребителското ви име .',
                                error_messages={
                                    'required': 'Това поле е задължително .',
                                    'password_mismatch': 'Паролите не съвпадат .'})

    password2 = forms.CharField(label='Потвърждение на парола',
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
                                error_messages={
                                    'required': 'Това поле е задължително .',})
    email = forms.EmailField(label='Електронна поща', error_messages={'invalid': 'Въведете валидна електронна поща !'})
    phone = forms.CharField(label='Мобилен телефон',
                            error_messages={'required': 'Въведете валиден мобилен номер'})

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Потребителско име',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label= 'Парола',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

