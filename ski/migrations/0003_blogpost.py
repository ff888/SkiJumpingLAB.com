# Generated by Django 4.2 on 2023-04-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski', '0002_tournamentfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post', models.TextField()),
            ],
        ),
    ]