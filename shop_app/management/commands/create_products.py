from django.core.management.base import BaseCommand
from shop_app.models import Product
from random import choice, randint
from datetime import datetime, timedelta
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Generate products (flowers)"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int,  help='count_products')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        with open('shop_app/data_lists/foods.txt', 'r', encoding='utf-8') as f:
            product_list = []
            for i in f:
                product_list.append(i)

        for _ in range(count):
            product = Product(
                name_product = choice(product_list)[:-1],
                description = lorem_ipsum.words(randint(50, 100), common=False),
                price = randint(100, 500),
                quantity = randint(0, 500),
                date_add = create_data()
            )
            product.save()
            self.stdout.write(f'{product.name_product}')

def create_data(start_date=datetime(2023, 1, 1)):
    end_date = datetime.now()
    random_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))
    return random_date