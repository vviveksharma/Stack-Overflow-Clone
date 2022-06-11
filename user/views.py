from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.forms import *
from django.contrib.auth.decorators import login_required
@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account is successfully created for {username}! Login Now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request , 'users/register.html',{
        'form': form
    })

@login_required
def profile(request):
    return render(request , 'users/profile.html')

@login_required
def update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST , instance=request.user)
        p_form = ProfileUpdateForm(request.POST , request.FILES , instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'Account is Updated Successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST , instance=request.user)
        p_form = ProfileUpdateForm(request.POST , request.FILES , instance=request.user.profile)
        context = {
            'u_form' : u_form,
            'p_form' : p_form
        }
        return render(request , 'users/update.html' , context)
