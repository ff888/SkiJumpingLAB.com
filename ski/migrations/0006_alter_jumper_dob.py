# Generated by Django 4.2 on 2023-04-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski', '0005_alter_jumper_distance_jump_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jumper',
            name='dob',
            field=models.CharField(max_length=255),
        ),
    ]
