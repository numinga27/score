# Generated by Django 3.1.10 on 2023-09-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hockeyliveevents',
            name='AWAY_SCORE_PART_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hockeyliveevents',
            name='AWAY_SCORE_PART_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hockeyliveevents',
            name='HOME_SCORE_PART_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hockeyliveevents',
            name='HOME_SCORE_PART_3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
