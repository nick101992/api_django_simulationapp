from django.db import models
from django.contrib.auth.models import User
from simulation_modelling.models import Simulation_Model

class Codesimul_Type(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Codesimul_Model(models.Model):
    name = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    codesimul_type = models.ForeignKey(Codesimul_Type,
                                   on_delete=models.CASCADE,
                                   related_name="code_type")
    simulation_model = models.ForeignKey(Simulation_Model,
                                   on_delete=models.CASCADE,
                                   related_name="simulation_models")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
