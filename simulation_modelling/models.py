from django.db import models
from django.contrib.auth.models import User
from system_modelling.models import System_Model

class Simulation_Type(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Simulation_Model(models.Model):
    name = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    simulation_type = models.ForeignKey(Simulation_Type,
                                   on_delete=models.CASCADE,
                                   related_name="models_type")
    system_model = models.ForeignKey(System_Model,
                                   on_delete=models.CASCADE,
                                   related_name="models_type")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
