# Generated by Django 3.2 on 2021-04-26 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation_experiment', '0003_simuloutput_model_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simuloutput_model',
            name='author',
        ),
    ]
