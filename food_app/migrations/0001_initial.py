# Generated by Django 4.0.4 on 2022-05-19 18:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('foodplace_uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UNIQUE ID FOR THE BATCH')),
                ('name', models.CharField(max_length=150)),
                ('owner_name', models.CharField(max_length=150)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnail')),
                ('location', models.CharField(max_length=500)),
                ('maps_location_link', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('rating', models.IntegerField(default=1)),
                ('spam', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('food_place', models.CharField(max_length=150)),
                ('review', models.TextField(max_length=500)),
                ('rating', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnail')),
                ('price', models.IntegerField(default=0)),
                ('special', models.BooleanField(default=False)),
                ('food_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_app.foodplace')),
            ],
        ),
    ]
