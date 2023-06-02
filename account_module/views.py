from random import choice
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from account_module.forms import AuthenticationForm, RegisterForm, ActivateForm, ForgetPasswordForm, ResetPasswordForm
from account_module.models import User
from utils.email_service import email_send


class LoginUserView(LoginView):
    template_name = 'account_module/login.html'
    form_class = AuthenticationForm


class RegisterUserView(View):
    def get(self, request: HttpRequest):
        register_form = RegisterForm
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            if User.objects.filter(email=register_form.cleaned_data.get('email')).first() is None:
                if User.objects.filter(username=register_form.cleaned_data.get('username')).first() is None:
                    email_active_code = choice(list(range(1000000, 10000000)))
                    while User.objects.filter(email_active_code=int(email_active_code)).first() is not None:
                        email_active_code = choice(list(range(1000000, 10000000)))
                    new_user = User(email=email, username=username, is_active=False,
                                    email_active_code=int(email_active_code), first_name=first_name,
                                    last_name=last_name)
                    new_user.set_password(password)
                    new_user.save()

                    context = {
                        'code': email_active_code,
                    }
                    email_send('فعال سازی حساب کاربری', email, context, 'emails/active_account.html')
                    return redirect(reverse('active-account'))
                else:
                    register_form.add_error('username', 'این نام کاربری قبلا وارد شده!')
            else:
                register_form.add_error('email', 'کاربری با این ایمیل قبلاً در سایت ثبت نام کرده است!')
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)


class ActiveAccountView(View):
    def get(self, request):
        context = {
            'form': ActivateForm,
        }
        return render(request, 'account_module/active_account.html', context)

    def post(self, request: HttpRequest):
        form = ActivateForm(request.POST)
        if form.is_valid():
            email_active_code = form.cleaned_data.get('email_active_code')
            user = User.objects.filter(email_active_code=email_active_code).first()
            if user is not None:
                user.email_active_code = choice(list(range(1000000, 10000000)))
                while User.objects.filter(email_active_code=int(user.email_active_code)).first() is not None:
                    user.email_active_code = choice(list(range(1000000, 10000000)))
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    return redirect('login-page')
                else:
                    user.save()
                    form.add_error('email_active_code', 'اکانت شما قبلا فعال شده است!')
                    context = {
                        'form': form,
                    }
                    return render(request, 'account_module/active_account.html', context)
            else:
                form.add_error('email_active_code', 'کد وارد شده اشتباه است!')
                context = {
                    'form': form,
                }
                return render(request, 'account_module/active_account.html', context)


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        reset_password = ForgetPasswordForm()
        context = {
            'reset_password': reset_password
        }
        return render(request, 'account_module/forget_password.html', context)

    def post(self, request: HttpRequest):
        reset_password = ForgetPasswordForm(request.POST)
        if reset_password.is_valid():
            user_email = reset_password.cleaned_data.get('email')
            user = User.objects.filter(email__exact=user_email).first()
            if user is not None:
                email = user.email
                context = {
                    'code': user.email_active_code
                }
                email_send('بازیابی رمز عبور', email, context, 'emails/reset_password.html')
                return redirect('reset-password')
            else:
                reset_password.add_error('email', 'ایمیل وارد شده پیدا نشد')

        context = {
            'reset_password': reset_password
        }
        return render(request, 'account_module/forget_password.html', context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest):
        context = {
            'form': ResetPasswordForm,
        }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request: HttpRequest):
        reset_password_form = ResetPasswordForm(request.POST)
        email_active_code = request.POST.get('email_active_code')
        if reset_password_form.is_valid():
            user = User.objects.filter(email_active_code__iexact=email_active_code).first()
            if user is not None:
                user_password = reset_password_form.cleaned_data.get('password')
                user.set_password(user_password)
                email_active_code = choice(list(range(1000000, 10000000)))
                while User.objects.filter(email_active_code=int(email_active_code)).first() is not None:
                    email_active_code = choice(list(range(1000000, 10000000)))
                user.email_active_code = email_active_code
                user.is_active = True
                user.save()
                return redirect('login-page')
            else:
                reset_password_form.add_error('email_active_code', 'کد فعالسازی نامعتبر می باشد!')
        context = {
            'form': reset_password_form,
        }
        return render(request, 'account_module/reset_password.html', context)