# Generated by Django 4.0.4 on 2022-05-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_foodplace_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodplace',
            name='rating',
            field=models.FloatField(default=1),
        ),
    ]
