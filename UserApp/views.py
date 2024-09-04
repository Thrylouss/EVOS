from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin')
        return redirect('main')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = authenticate(request, username, password)
            login(request, user)
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'UserApp/signup.html', context)


def sign_in(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin')
        return redirect('main')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if request.user.is_staff:
                return redirect('admin')
            return redirect('main')
    form = LoginForm()
    context = {'form': form}
    return render(request, 'UserApp/login.html', context)


def log_out(request):
    logout(request)
    return redirect('signIn')
