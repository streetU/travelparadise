# Generated by Django 3.1.2 on 2022-10-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0005_auto_20221013_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='arrival_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_date',
            field=models.DateField(default=None),
        ),
    ]