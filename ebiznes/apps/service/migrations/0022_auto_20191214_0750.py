# Generated by Django 2.2.8 on 2019-12-14 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_auto_20191214_0744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'price', 'verbose_name_plural': 'price'},
        ),
        migrations.AlterModelOptions(
            name='pricelist',
            options={'verbose_name': 'price', 'verbose_name_plural': 'price'},
        ),
    ]