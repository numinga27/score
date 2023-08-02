# Generated by Django 2.2.16 on 2023-07-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='an',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_event_participant_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_images',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_name',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_participant_ids',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_participant_name_one',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_participant_types',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_score_current',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_score_part_1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='away_score_part_2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='bookmakers_with_live_in_offer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='home_participant_ids',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='imm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='imp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='imw',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='live_mark',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='merge_stage_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='rounds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='shortname_away',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='shortname_home',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='sort',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='stage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='stage_start_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='stage_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_utime',
            field=models.IntegerField(),
        ),
    ]