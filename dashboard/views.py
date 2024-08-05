from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrdersForm
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your views here.
@login_required
def index(request):
    products = Product.objects.exclude(do_number=None) # to filter those that are no DO_Number
    products_count = products.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = OrdersForm()
    context = {
        'products' : products,
        'form' : form,
        'workers_count' : workers_count,
        'products_count' : products_count,
        'orders_count' : orders_count,
    }
    #return HttpResponse('<h1 style="color:red;">This is the Index Page</h1>')
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    products_count = Product.objects.exclude(do_number=None).count()
    orders_count = Order.objects.all().count()
    context = {
        'workers' : workers,
        'workers_count' : workers_count,
        'products_count' : products_count,
        'orders_count' : orders_count,
    }
    #return HttpResponse('This is the Staff Page')
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_view(request, pk):
    workers = User.objects.get(id=pk)
    workers_count = User.objects.all().count()
    products_count = Product.objects.exclude(do_number=None).count()
    orders_count = Order.objects.all().count()
    context = {
        'workers' : workers,
        'workers_count' : workers_count,
        'products_count' : products_count,
        'orders_count' : orders_count,
    }
    return render(request, 'dashboard/staff_view.html', context)

@login_required
def staff_delete(request, pk): #pk = primary_key, so that the particular item can be deleted
    workers = User.objects.get(id=pk)
    if request.method == 'POST':
        workers.delete()
        return redirect('dashboard-staff')
    return render(request, 'dashboard/staff_delete.html')

@login_required
def product(request):
    # products = Product.objects.raw('SELECT * FROM dashboard_product') # using SQL
    # products = Product.objects.all() # using ORM
    products = Product.objects.exclude(do_number=None) # to filter those that are no DO_Number
    products_count = products.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    context = {
        'products' : products,
        'workers_count' : workers_count,
        'products_count' : products_count,
        'orders_count' : orders_count,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_status(request): #pk = primary_key, so that the particular item can be deleted
    products = Product.objects.all() # using ORM
    products_count = products.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product-status')
    else:
        form = ProductForm()
    # Fetch products and aggregate quantities
    # aggregated_products = (
    # Product.objects.all()
    # .values('company', 'item')  # Group by company and item
    # .annotate(total_qty=Sum('qty'))  # Sum up the quantities
    # )
    context = {
        'products' : products,
        'form': form,
        'products_count' : products_count,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        # 'aggregated_products': aggregated_products,
    }
    return render(request, 'dashboard/product_status.html', context)


@login_required
def product_delete(request, pk): #pk = primary_key, so that the particular item can be deleted
    products = Product.objects.get(id=pk)
    if request.method == 'POST':
        products.delete()
        return redirect('dashboard-product-status')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    products = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=products) # instance=product, to pre-fill
        if form.is_valid():
            form.save()
            return redirect('dashboard-product-status')
    else:
        form = ProductForm(instance=products)
    context ={
        'form' : form
    }
    return render(request, 'dashboard/product_update.html',context)

@login_required
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    products_count = Product.objects.exclude(do_number=None).count()
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-order')
    else:
        form = OrdersForm()
    context = {
        'orders' : orders,
        'form': form,
        'workers_count' : workers_count,
        'products_count' : products_count,
        'orders_count' : orders_count,
    }
    return render(request, 'dashboard/order.html', context)

@login_required
def order_delete(request, pk): #pk = primary_key, so that the particular item can be deleted
    orders = Order.objects.get(id=pk)
    if request.method == 'POST':
        orders.delete()
        return redirect('dashboard-order')
    return render(request, 'dashboard/order_delete.html')

@login_required
def order_update(request, pk):
    orders = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=orders) # instance=order, to pre-fill
        if form.is_valid():
            form.save()
            return redirect('dashboard-order')
    else:
        form = OrdersForm(instance=orders)
    context ={
        'form' : form
    }
    return render(request, 'dashboard/order_update.html',context)