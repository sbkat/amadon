from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process_checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product_id = Product.objects.get(id=float(request.POST["product_id"]))
    price_from_form = product_id.price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    context = {
        "this_order": Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge),
    }
    return redirect('/checkout', context)

def checkout(request):
    all_orders = Order.objects.all()
    overall_price = 0
    overall_quantity = 0
    
    for order in all_orders:
        overall_price += order.total_price
        overall_quantity += order.quantity_ordered
    print(overall_price)
    print(overall_quantity)
    print(order.total_price)

    context = {
        "overall_price": overall_price,
        "overall_quantity": overall_quantity,
        "order_price": order.total_price,
    }
    return render(request, "store/checkout.html", context)
    