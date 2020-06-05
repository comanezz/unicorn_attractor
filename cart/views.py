from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required()
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")