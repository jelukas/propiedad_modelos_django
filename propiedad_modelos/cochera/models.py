from django.db import models
from django_extras.contrib.auth.models import SingleOwnerMixin


# Un coche tiene un solo propietario
class Coche(SingleOwnerMixin, models.Model):
	marca = models.CharField(max_length=200)
	modelo = models.CharField(max_length=200)

	def __unicode__(self):
		return self.marca + ' - ' + self.modelo