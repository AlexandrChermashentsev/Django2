from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_registration = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to = 'media/')

    def __str__(self) -> str:
        return self.name_product

   
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    order_date = models.DateField()

    def __str__(self) -> str:
        return f'Purchase from {self.order_date}'