# Generated by Django 3.1.10 on 2023-09-20 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0013_auto_20230919_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hockeyliveevents',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='scoreflash.tournamenthockey'),
        ),
    ]
