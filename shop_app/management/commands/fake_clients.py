from django.core.management.base import BaseCommand
from shop_app.models import Client
from random import choice, randint
from datetime import datetime, timedelta

mail_list = ['mail.ru', 'gmail.com', 'outlook.com', 'yahoo.com', 'rambler.ru', 'yandex.ru']


class Command(BaseCommand):
    help = "Generate clients"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int,  help='count_clients')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        with open('shop_app/data_lists/names.txt', 'r', encoding='utf-8') as f:
            names_list = []
            for i in f:
                names_list.append(i)

        with open('shop_app/data_lists/second_names.txt', 'r', encoding='utf-8') as f:
            second_names_list = []
            for i in f:
                second_names_list.append(i)

        for i in range(count):
            f_n = choice(names_list).capitalize()[:-1]
            s_n = choice(second_names_list)
            client = Client(
                name = f_n + " " + s_n,
                email = f"{f_n}_{s_n}@{choice(mail_list)}",
                phone_number = generate_phone_number(),
                address = generate_addres(),
                date_registration = create_data())
            client.save()
            self.stdout.write(f'{client.name}')


def create_data():
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))
    return random_date


def generate_phone_number():
    number = '89'
    for _ in range(9):
        number += str(randint(0, 9))
    return number


def generate_addres():
    cities_list = []
    streets_list = []

    with open('shop_app/data_lists/cities.txt', 'r', encoding='utf-8') as f:
        for i in f:
            cities_list.append(i)
            
    with open('shop_app/data_lists/streets.txt', 'r', encoding='utf-8') as f:
        for i in f:
            streets_list.append(i)

    addres = f'{choice(cities_list)[:-1]}, {choice(streets_list)[:-1]}, {randint(1, 200)}'
    return addres