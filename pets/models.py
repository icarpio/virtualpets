from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class PetBase(models.Model):
    name = models.CharField(max_length=50)
    base_image = models.URLField()
    evolution1_image = models.URLField()
    evolution2_image = models.URLField()
    
    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_base = models.ForeignKey(PetBase, on_delete=models.SET_NULL, null=True)
    hunger = models.IntegerField(default=60)  # Inicialmente en un valor bajo
    energy = models.IntegerField(default=60)
    happiness = models.IntegerField(default=60)
    current_image = models.URLField()  # URL de la imagen actual
    evolution_stage = models.IntegerField(default=0)  # 0 - Base, 1 - Evolución 1, 2 - Evolución 2
    last_interaction = models.DateTimeField(default=timezone.now)  # Fecha de última interacción

    def evolve(self):
        """Comprueba si la mascota puede evolucionar y cambia su estado si es posible."""
        now = timezone.now()

        if self.evolution_stage == 0 and self.hunger >= 80 and self.energy >= 80 and self.happiness >= 80:
            if self.last_interaction <= now - timedelta(hours=3):
                self.evolution_stage = 1
                self.current_image = self.pet_base.evolution1_image
                self.last_interaction = now
                self.save()
                return "¡Tu mascota ha evolucionado a la etapa 1!"
        elif self.evolution_stage == 1 and self.hunger >= 90 and self.energy >= 90 and self.happiness >= 90:
            if self.last_interaction <= now - timedelta(hours=5):
                self.evolution_stage = 2
                self.current_image = self.pet_base.evolution2_image
                self.last_interaction = now
                self.save()
                return "¡Tu mascota ha evolucionado a la etapa 2!"
        return "No se cumplen los requisitos para evolucionar."


    def __str__(self):
        return self.name
