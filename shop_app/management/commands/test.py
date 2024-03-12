from random import choice, randint
from datetime import datetime, timedelta


def create_data(start_date=datetime(2023, 1, 1)):
    end_date = datetime.now()
    random_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))
    return random_date

print(create_data())