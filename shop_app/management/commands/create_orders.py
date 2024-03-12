from django.core.management.base import BaseCommand
from shop_app.models import Product, Client, Order
from random import choice, randint
from datetime import datetime, timedelta
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = "Generate orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int,  help='count_orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()
        products = Product.objects.all()

        for _ in range(count):
            # _client = choice(clients)
            _product = choice(products)

            dt = datetime.combine(_product.date_add, datetime.min.time())

            order = Order(
                client = choice(clients),
                product = _product,
                product_price = _product.price,
                total_amount = randint(1, _product.quantity) * _product.price,
                order_date = create_data(dt)
            )
            order.save()
            self.stdout.write(f'{order.client} | {order.product} | {order.total_amount} | {order.order_date}')

def generate_all_price(product: Product):
    total_amount = randint(1, product.quantity) * product.price
    return total_amount

def create_data(start_date=datetime(2023, 1, 1)):
    end_date = datetime.now()
    random_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))
    return random_date