# Generated by Django 4.1.5 on 2023-01-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_orderitem_order_remove_orderitem_product_and_more'),
        ('cart', '0004_alter_order_address_alter_order_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_list',
        ),
        migrations.AddField(
            model_name='order',
            name='order_list',
            field=models.ManyToManyField(null=True, to='store.product', verbose_name='Состав заказа'),
        ),
    ]
