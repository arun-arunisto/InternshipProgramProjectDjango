from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def candidate_signup(request):
    return render(request, "candidate_signup.html")

def candidate_login(request):
    return render(request, "candidate_login.html")

def application_form(request):
    return render(request, "application_form.html")

def application_status(request):
    return render(request, "application_status.html")