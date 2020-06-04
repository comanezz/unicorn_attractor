from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def all_features(request):
    """ View all feature list
    """
    return render(request, "features.html",)