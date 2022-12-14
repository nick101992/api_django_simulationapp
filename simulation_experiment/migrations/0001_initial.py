# Generated by Django 3.2 on 2021-04-26 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simulation_code', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulation_Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Simulexp_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('simulation_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simulation_codes', to='simulation_code.codesimul_model')),
                ('simulation_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simul_engine', to='simulation_experiment.simulation_engine')),
            ],
        ),
        migrations.CreateModel(
            name='SimulOutput_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_name', models.CharField(max_length=140)),
                ('value', models.FloatField(max_length=80)),
                ('simulation_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simulexp', to='simulation_experiment.simulexp_model')),
            ],
        ),
    ]
