# Generated by Django 2.2.16 on 2023-08-24 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0002_hockeyliveevents_tournamenthockey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('away_yellow', models.TextField(null=True)),
                ('away_red', models.TextField(null=True)),
                ('home_yellow', models.TextField(null=True)),
                ('home_red', models.TextField(null=True)),
                ('events_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_cards', to='scoreflash.EventId')),
            ],
        ),
    ]
