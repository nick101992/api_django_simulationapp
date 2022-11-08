# Generated by Django 3.2 on 2021-04-26 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simulation_experiment', '0002_alter_simuloutput_model_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='simuloutput_model',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
