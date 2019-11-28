# Generated by Django 2.2.5 on 2019-11-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_auto_20191120_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='status',
            field=models.CharField(choices=[('WAITING_FOR_APPROVAL', 'Waiting for approval'), ('NOT_APPROVED', 'Not approved'), ('APPROVED', 'Approved'), ('DONE', 'Done')], default='WAITING_FOR_APPROVAL', max_length=100, verbose_name='Status'),
        ),
    ]