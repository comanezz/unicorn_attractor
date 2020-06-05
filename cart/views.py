from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required()
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

@login_required()
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""

    # Not using a form inside the feature detail html page so need to set up the quantity in the view page.
    quantity = 1

    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect('all_features')