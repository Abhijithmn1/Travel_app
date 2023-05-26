from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME ALREDY TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "MAIL ID ALREDY TAKEN")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname,
                                                last_name=lastname, email=email, password=password)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, "Password not match")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
