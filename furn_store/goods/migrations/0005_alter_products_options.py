# Generated by Django 4.2.7 on 2024-04-22 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_products_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]