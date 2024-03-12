from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Client, Order, Product
from.forms import ClientForm, ProductForm
from django.core.files.storage import FileSystemStorage


def customer_orders(request, client_id):
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client_id=client)
    return render(request, 'shop_app/orders.html', {'client': client, 'orders': orders})


def hello(request):
    return render(request, "shop_app/index.html")


def show_client(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'shop_app/client.html', {'client': client})


def client_form(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Client.objects.create(
                name=data['name'],
                email=data['email'],
                phone_number=data['phone_number'],
                address=data['address'],
                date_registration=data['date_registration'],
                )
            return redirect('form')
    else:
        form = ClientForm()
    return render(request, 'shop_app/form.html', {'form': form})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            img=form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(img.name, img)
            Product.objects.create(
                name_product=form.cleaned_data['name_product'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                date_add=form.cleaned_data['date_add'],
                image=img
            )
            return redirect('form.html')
    else:
        form = ProductForm()
    return render(request, 'shop_app/form.html', {'form': form})


def img_view(request, img):
    img_data = open(f"media/media/{img}", 'rb', encoding='UTF-8').read()
    return HTTPResponse(img_data)