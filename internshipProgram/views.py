from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def candidate_signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=email)
            messages.error(request, "Email already registered!")
        except User.DoesNotExist:
            try:
                applicant = User.objects.create_user(username=username,
                                                     email=email,
                                                     password=password)
                applicant.save()
                messages.info(request, "Registered Successfully!!")
                return redirect('candidate_login')
            except:
                messages.error(request, "Username already registered!")
    return render(request, "candidate_signup.html")

def candidate_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Login Successfully!!")
            return redirect('home')
        messages.error(request, "Email/Password incorrect!!")
    return render(request, "candidate_login.html")

@login_required
def application_form(request):
    return render(request, "application_form.html")

@login_required
def application_status(request):
    return render(request, "application_status.html")

@login_required
def candidate_logout(request):
    logout(request)
    return redirect('home')