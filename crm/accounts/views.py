from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CustomerForm, CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .mydecorators import anonymous, allowed_users, admin_only

from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all().order_by('-id')
    customers = Customer.objects.all()
    total_orders = orders.count()
    delivered = Order.objects.all().filter(status='Delivered').count()
    pending = Order.objects.all().filter(status='Pending').count()
    out = Order.objects.all().filter(status='Out For Delivery').count()
    datas = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'out': out
        
    }
    return render(request, 'accounts/index.html', datas)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    datas = {
        'products': products
    }
    return render(request, 'accounts/products.html',datas)


@login_required(login_url='login')
@allowed_users(allowed_roles='customer')
def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = Order.objects.filter(customer=customers) 
    total_orders = orders.count()
    datas = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        
    }
    return render(request, 'accounts/customers.html', datas)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=['product', 'status'])
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    datas = {
        'formset': formset,
        
        
    }
    return render(request, 'accounts/create-order.html', datas)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('/')
    
    
    
    datas = {
        'form': form
    }
    return render(request, 'accounts/create-order.html', datas)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    datas = {
        'item': order
    }
    return render(request, 'accounts/delete-order.html', datas)


@login_required
@allowed_users(allowed_roles='admin')
def createCustomer(request):
    
    form = CustomerForm()
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    
    datas = {
        'form': form
    }
    return render(request, 'accounts/create-customer.html', datas)

@anonymous
def registerUser(request):
    form = CreateUser()
    
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid:
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'+ Account {username} successfully  created')
            return redirect('home')
    
    
    datas={
        'form':form
    }
    return render(request, 'accounts/register.html', datas)

@anonymous
def loginUser(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Password or Username may be incorrect')
    
    
    datas = {
        
    }
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userPage(request):
    
    #customer = Customer.objects.get(id=pk)
    customer = Customer.objects.filter(user=request.user)[0]
    orders = Order.objects.filter(customer=customer)
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out = orders.filter(status='Out For Delivery').count()
    
    print('userpage ', request.user.is_active)
    
    datas = {
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'out': out,
        'customer': customer
        
    }
    return render(request, 'accounts/user.html', datas)

@login_required(login_url='login')
def Usettings(request):
    customer= request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    
    
    datas = {
        'form': form,
    }
    return render(request, 'accounts/user-settings.html', datas)

