from django.db import models

# Create your models here.

class BasePeriod(models.Model):
	date_created = models.DateField()
	class Meta:
		abstract = True