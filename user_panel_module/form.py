from django import forms
from account_module.models import User
from django.core.exceptions import ValidationError


class UserEditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'avatar', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

        error_messages = {
            'username': {'unique': 'کاربری با نام کاربری وارد شده وجود دارد'}
        }


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='پسورد فعلی',
        max_length=300,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))
    new_password = forms.CharField(
        label='پسورد جدید',
        max_length=300,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))
    confirm_password = forms.CharField(
        label='تکرار پسورد جدید',
        max_length=300,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            pass
        else:
            raise ValidationError('کلمه عبور با تکرار کلمه عبور مغایرت دارد')