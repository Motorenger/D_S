# Generated by Django 4.0.6 on 2022-10-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_cart_cartproductsm2m_cart_products_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
