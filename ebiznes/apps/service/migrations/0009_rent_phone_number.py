# Generated by Django 2.2.5 on 2019-11-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]