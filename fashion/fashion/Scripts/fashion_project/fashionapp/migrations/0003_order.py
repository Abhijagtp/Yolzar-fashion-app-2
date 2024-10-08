# Generated by Django 5.1 on 2024-08-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0002_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('town_city', models.CharField(max_length=30)),
                ('country_state', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('accountpassword', models.TextField(max_length=300)),
                ('suggestions', models.CharField(max_length=30)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
