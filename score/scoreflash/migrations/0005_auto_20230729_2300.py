# Generated by Django 2.2.16 on 2023-07-29 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0004_auto_20230729_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liveofevents',
            old_name='events',
            new_name='event_id',
        ),
    ]
