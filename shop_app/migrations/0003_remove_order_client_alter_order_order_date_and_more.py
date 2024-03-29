# Generated by Django 5.0.2 on 2024-03-02 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_app", "0002_alter_product_date_add"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="client",
        ),
        migrations.AlterField(
            model_name="order",
            name="order_date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name="order",
            name="product",
        ),
        migrations.AddField(
            model_name="order",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop_app.client",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop_app.product",
            ),
        ),
    ]
