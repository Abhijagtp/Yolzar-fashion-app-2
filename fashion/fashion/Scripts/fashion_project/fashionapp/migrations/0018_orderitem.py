# Generated by Django 5.1 on 2024-08-31 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0017_orderyolzar_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='fashionapp.orderyolzar')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fashionapp.product')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
    ]
