# Generated by Django 2.2.5 on 2019-11-28 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_rent_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total price'),
        ),
    ]
