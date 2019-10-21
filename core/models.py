from django.db import models

class City(models.Model):
	name = models.CharField(max_length = 50)
	country = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'cities'

	def __str__(self):
		return self.name
