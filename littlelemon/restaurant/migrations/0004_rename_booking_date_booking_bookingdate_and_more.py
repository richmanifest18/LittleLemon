# Generated by Django 5.0.6 on 2024-06-12 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_bookingdate_booking_booking_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Booking_Date',
            new_name='bookingDate',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='No_of_guests',
            new_name='no_of_guests',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Inventory',
            new_name='inventory',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Title',
            new_name='title',
        ),
    ]