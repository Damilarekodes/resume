# Generated by Django 3.2.8 on 2022-06-22 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20220622_0513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='is_image',
        ),
    ]
