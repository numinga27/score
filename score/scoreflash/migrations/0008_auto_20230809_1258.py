# Generated by Django 2.2.16 on 2023-08-09 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0007_eventid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='an',
            new_name='short_name_away',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='away_event_participant_id',
            new_name='short_name_home',
        ),
        migrations.RemoveField(
            model_name='events',
            name='away_goal_var',
        ),
        migrations.RemoveField(
            model_name='events',
            name='away_participant_ids',
        ),
        migrations.RemoveField(
            model_name='events',
            name='away_participant_name_one',
        ),
        migrations.RemoveField(
            model_name='events',
            name='away_participant_types',
        ),
        migrations.RemoveField(
            model_name='events',
            name='away_score_full',
        ),
        migrations.RemoveField(
            model_name='events',
            name='bookmakers_with_live_in_offer',
        ),
        migrations.RemoveField(
            model_name='events',
            name='has_lineps',
        ),
        migrations.RemoveField(
            model_name='events',
            name='has_live_centre',
        ),
        migrations.RemoveField(
            model_name='events',
            name='home_event_participant_id',
        ),
        migrations.RemoveField(
            model_name='events',
            name='home_goal_var',
        ),
        migrations.RemoveField(
            model_name='events',
            name='home_participant_ids',
        ),
        migrations.RemoveField(
            model_name='events',
            name='home_participant_name_one',
        ),
        migrations.RemoveField(
            model_name='events',
            name='home_participant_types',
        ),
        migrations.RemoveField(
            model_name='events',
            name='ime',
        ),
        migrations.RemoveField(
            model_name='events',
            name='imm',
        ),
        migrations.RemoveField(
            model_name='events',
            name='imp',
        ),
        migrations.RemoveField(
            model_name='events',
            name='imw',
        ),
        migrations.RemoveField(
            model_name='events',
            name='live_in_offer_bookmaker_id',
        ),
        migrations.RemoveField(
            model_name='events',
            name='live_in_offer_status',
        ),
        migrations.RemoveField(
            model_name='events',
            name='live_mark',
        ),
        migrations.RemoveField(
            model_name='events',
            name='merge_stage_type',
        ),
        migrations.RemoveField(
            model_name='events',
            name='playing_on_sets',
        ),
        migrations.RemoveField(
            model_name='events',
            name='recent_overs',
        ),
        migrations.RemoveField(
            model_name='events',
            name='rounds',
        ),
        migrations.RemoveField(
            model_name='events',
            name='score_chance_away',
        ),
        migrations.RemoveField(
            model_name='events',
            name='shortname_away',
        ),
        migrations.RemoveField(
            model_name='events',
            name='shortname_home',
        ),
        migrations.RemoveField(
            model_name='events',
            name='sort',
        ),
        migrations.RemoveField(
            model_name='events',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='events',
            name='stage_start_time',
        ),
        migrations.RemoveField(
            model_name='events',
            name='stage_type',
        ),
        migrations.RemoveField(
            model_name='events',
            name='tv_live_streaming',
        ),
        migrations.RemoveField(
            model_name='events',
            name='visible_run_rate',
        ),
    ]
