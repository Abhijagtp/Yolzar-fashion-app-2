# Generated by Django 5.1 on 2024-08-31 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0011_remove_cart_quantity_remove_orderyolzar_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
