from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# def index(request):
#    return render(request, "BBWebsite/index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['company']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('selector') # replace 'home' with your desired redirect url
        else:
            error_message = 'Invalid login credentials'
    else:
        error_message = ''
    return render(request, 'BBWebsite/index.html', {'error_message': error_message})

def signup_view(request):
    return render(request, "BBWebsite/Account.html")

def personality_view(request):
    return render(request, "BBWebsite/personality.html")

def internship_view(request):
    if request.method == 'POST':
        company = request.POST['company']
        location = request.POST['location']
        season = request.POST['season']
        budget = request.POST['budget']
        
        if budget is not None:
            login(request, user)
            return redirect('selector') # replace 'home' with your desired redirect url
        else:
            error_message = 'Invalid login credentials'
    return render(request, "BBWebsite/internship.html")

def selector_view(request):
    return render(request, "BBWebsite/Selector.html")
