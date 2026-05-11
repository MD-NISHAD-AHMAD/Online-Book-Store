import json
from .models import *

def cartData(request):  
    # Check if the user is authenticated and has a customer object

    if request.user.is_authenticated:
        customer = request.user.customer if hasattr(request.user, 'customer') else None

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    return {'cartItems': cartItems, 'items': items, 'order': order}
