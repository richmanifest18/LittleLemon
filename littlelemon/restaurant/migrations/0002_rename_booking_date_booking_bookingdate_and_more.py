# Generated by Django 5.0.6 on 2024-06-12 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date',
            new_name='BookingDate',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='number_of_guests',
            new_name='No_of_guests',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='inventory',
            new_name='Inventory',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='title',
            new_name='Title',
        ),
    ]
