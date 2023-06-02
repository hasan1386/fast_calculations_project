from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from user_panel_module.form import UserEditProfileModelForm, ChangePasswordForm


@method_decorator(login_required, name='dispatch')
class UserPanelModule(TemplateView):
    template_name = 'user_panel_module/user_panel.html'


@method_decorator(login_required, name='dispatch')
class UserEditProfileView(View):
    def get(self, request: HttpRequest):
        current_user: User = User.objects.filter(id=request.user.id).first()
        edit_form = UserEditProfileModelForm(instance=current_user)
        context = {
            'form': edit_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/information.html', context)

    def post(self, request: HttpRequest):
        current_user: User = User.objects.filter(id=request.user.id).first()
        edit_form = UserEditProfileModelForm(request.POST, request.FILES, instance=current_user)
        success = False
        if edit_form.is_valid():
            edit_form.save(commit=True)
            success = True
        context = {
            'form': edit_form,
            'current_user': current_user,
            'success': success,
        }
        return render(request, 'user_panel_module/information.html', context)


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    def get(self, request):
        form = ChangePasswordForm()
        context = {
            'form': form
        }
        return render(request, 'user_panel_module/change_password.html', context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            user = User.objects.filter(id=request.user.id).first()
            if user is not None:
                check_password = user.check_password(old_password)
                if check_password:
                    user.set_password(new_password)
                    user.save()
                    logout(request)
                    login(request, user)
                    return redirect('user-edit-profile')
                else:
                    form.add_error('old_password', 'پسورد وارد شده صحیح نمی باشد')
                    context = {
                        'form': form
                    }
                    return render(request, 'user_panel_module/change_password.html', context)
        else:
            context = {
                'form': form
            }
            return render(request, 'user_panel_module/change_password.html', context)