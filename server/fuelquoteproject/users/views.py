from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from users.forms import UserChangeForm
from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm

#Create your views here.

class Register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "pages/register.html"

def userProfile(request):
    context = {
        "user": request.user
    }
    return render(request, 'pages/profile.html', context)

def edit_userProfile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            print('Form saved successfully')
            return redirect('/users/profile')
        else:
            form = CustomUserChangeForm(instance=request.user)
            context = {
                "form": form,
            }
            return render(request, 'pages/edit_profile.html', context)

    else:
        form = CustomUserChangeForm(instance=request.user)
        context = {
            "form": form,
        }
        return render(request, 'pages/edit_profile.html', context)
