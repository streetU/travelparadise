# Generated by Django 3.1.2 on 2022-10-13 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0013_auto_20221013_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segment',
            old_name='segid',
            new_name='id',
        ),
    ]
