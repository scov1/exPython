from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from carApp.models import Car


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Введеные данные не верные!")
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Данный логин занят')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Данный email занят')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=pass1, email=email)
                user.save()
                messages.info(request, 'Пользователь создан')
                return redirect('login')
        else:
            messages.info(request, 'Пароль не верный')
            return redirect('register')

        return redirect('/')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
