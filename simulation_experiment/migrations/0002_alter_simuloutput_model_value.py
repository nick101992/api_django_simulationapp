# Generated by Django 3.2 on 2021-04-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation_experiment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simuloutput_model',
            name='value',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]