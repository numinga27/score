# Generated by Django 2.2.16 on 2023-07-29 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0005_auto_20230729_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liveofevents',
            name='an',
        ),
        migrations.RemoveField(
            model_name='liveofevents',
            name='live_in_offer_book_id',
        ),
        migrations.RemoveField(
            model_name='liveofevents',
            name='live_in_offer_status',
        ),
    ]
