# Generated by Django 5.0.2 on 2024-03-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_app", "0005_product_image_alter_client_date_registration_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=models.CharField(max_length=15),
        ),
    ]
