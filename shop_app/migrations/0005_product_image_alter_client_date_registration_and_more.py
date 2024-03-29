# Generated by Django 5.0.2 on 2024-03-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_app", "0004_rename_all_price_order_product_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(default=2021, upload_to=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="client",
            name="date_registration",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="date_add",
            field=models.DateField(auto_now_add=True),
        ),
    ]
