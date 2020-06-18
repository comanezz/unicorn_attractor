from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Bug
from features.models import Feature

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!", extra_tags="alert alert-success")
    return redirect(reverse('index'))

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!", extra_tags="alert alert-success")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            # once weve created the user then we're just going to log the user in
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            # Once the user has been authenticated we can log him in
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered", extra_tags="alert alert-success")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time", extra_tags="alert alert-danger")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {"registration_form": registration_form})

@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    bugs = Bug.objects.filter(author=request.user)
    features = Feature.objects.filter(author=request.user)
    return render(request, 'profile.html', {"profile": user, "bugs": bugs, "features": features})