from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, EditUserForm
from .models import *
from django.contrib import messages


# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)

        if form.is_valid():
            print("yes valid")
            # print(request.FILES)
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('list_users')

    context = {'form': form, 'edit': False}
    return render(request, 'users/add_edit_user.html', context=context)


@login_required(login_url='login')
def list_users(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'users/list_users.html', context=context)


def log_in_user(request):
    if request.user.is_authenticated:
        return redirect('list_users')
    else:
        if request.method == 'POST':
            username = request.POST.get('unm')
            password = request.POST.get('pwd')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('list_users')
            else:
                messages.info(request, 'email OR password is incorrect')

    return render(request, 'users/login.html')


def log_out_user(request):
    logout(request)
    return redirect('login')


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():

            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, 'Updated Details for User: ' + user_name)

            return redirect('list_users')

    form = EditUserForm(instance=user)
    context = {'form': form, 'edit': True}
    return render(request, 'users/add_edit_user.html', context=context)
