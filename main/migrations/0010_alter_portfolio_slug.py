# Generated by Django 3.2.8 on 2022-06-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_skill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.URLField(blank=True, null=True),
        ),
    ]
