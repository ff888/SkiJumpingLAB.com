# Generated by Django 4.2 on 2023-04-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski', '0004_rename_post_blogpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jumper',
            name='distance_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='distance_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='distance_points_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='distance_points_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='gate_compensation_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='gate_compensation_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='gate_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='gate_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_a_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_a_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_b_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_b_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_c_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_c_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_d_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_d_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_e_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_marks_e_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_total_points_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='judge_total_points_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='ranking',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='ranking_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='ranking_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='speed_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='speed_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='team_points',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='team_ranking',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='total_points',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='total_points_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='total_points_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='wind_compensation_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='wind_compensation_jump_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='wind_jump_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jumper',
            name='wind_jump_2',
            field=models.CharField(max_length=255),
        ),
    ]
