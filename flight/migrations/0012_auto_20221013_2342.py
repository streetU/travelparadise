# Generated by Django 3.1.2 on 2022-10-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0011_segment_seg_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segment',
            name='id',
        ),
        migrations.AlterField(
            model_name='segment',
            name='seg_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
