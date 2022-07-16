from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm,EditProfileForm
from datetime import datetime

from .models import Register


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('lists')

    page = 'register'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            if user.username.count("'") > 0:
                messages.error(request, 'only alphabet allowed for username')
            elif user.first_name.count("'") > 0:
                messages.error(request, 'only alphabet allowed for fullname')
            else:
                form.save()
                login(request, user)
                messages.success(request, 'Account created successfully')
                return redirect('edit-account')
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('lists')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username dont exist')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You Have Login successfully')
            return redirect('lists')
        else:
            messages.error(request,'username or password is incorrect')

    return render(request, 'users/login_register.html')



def logoutPage(request):
    logout(request)
    messages.info(request, 'You Have Logout successfully')
    return redirect('login')

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.register
    toplist = profile.todo_set.filter(time_reminder__gt=datetime.now())
    context = {'profile':profile,'toplist':toplist}
    return render(request, 'users/user_account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.register
    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Updated successfully')
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/edit_profile.html',context)


@login_required(login_url='login')
def deleteAccount(request):
    profile = request.user.register
    account = Register.objects.get(username=profile)
    if request.method == 'POST':
        account.delete()
        return redirect('login')
    context = {'account':account}
    return render(request, 'users/delete_account.html', context)


def usersProfiles(request):
    user=request.user.register
    profiles = Register.objects.exclude(username=user)
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html',context)


def singleProfile(request,pk):
    user=request.user.register
    profile = Register.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'users/single_profile.html',context)






