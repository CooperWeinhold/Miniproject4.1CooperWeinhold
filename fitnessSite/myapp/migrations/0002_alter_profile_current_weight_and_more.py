# Generated by Django 5.1.3 on 2024-11-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='goal_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timeline',
            field=models.IntegerField(default=0),
        ),
    ]
