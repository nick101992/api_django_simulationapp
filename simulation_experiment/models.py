from django.db import models
from django.contrib.auth.models import User
from simulation_code.models import Codesimul_Model

class Simulation_Engine(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Simulexp_Model(models.Model):
    name = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    simulation_engine = models.ForeignKey(Simulation_Engine,
                                   on_delete=models.CASCADE,
                                   related_name="simul_engine")
    simulation_code = models.ForeignKey(Codesimul_Model,
                                   on_delete=models.CASCADE,
                                   related_name="simulation_codes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SimulOutput_Model(models.Model):
    variable_name = models.CharField(max_length=140)
    value = models.DecimalField(max_digits=19, decimal_places=10)
    simulation_exp = models.ForeignKey(Simulexp_Model,
                                   on_delete=models.CASCADE,
                                   related_name="simulexp")

    def __str__(self):
        return self.variable_name
