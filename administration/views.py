from django.shortcuts import render

# Create your views here.
def administrative_index(request):
    return render(request, 'administrative_index.html')

def administrative_signup(request):
    return render(request, 'administrative_signup.html')

def administrative_home(request):
    return render(request, 'administrative_home.html')

def candidates_list(request):
    return render(request, 'candidates_list.html')

def administrative_profile(request):
    return render(request, 'administrative_profile.html')

def selected_candidates(request):
    return render(request, 'selected_candidates.html')

def rejected_candidates(request):
    return render(request, 'rejected_candidates.html')