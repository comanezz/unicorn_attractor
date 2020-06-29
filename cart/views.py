from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


@login_required()
def add_to_cart(request, id):
    """Add a quantity of the specified feature to the cart, not more than 1"""

    # Not using a form inside the feature detail html page
    # so need to set up the quantity in the view page.
    quantity = 1

    cart = request.session.get('cart', {})

    # https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
    if id in cart.keys():
        messages.error(
            request,
            "Feature already added",
            extra_tags="alert alert-danger")
    else:
        cart[id] = cart.get(id, quantity)
        messages.success(
            request,
            "Feature successfully added to the cart",
            extra_tags="alert alert-success")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


@login_required()
def delete_item(request, id):
    """
    Remove the item
    """
    cart = request.session.get('cart', {})

    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
