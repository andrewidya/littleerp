from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Provinces(models.Model):
	name = models.CharField(verbose_name=_('Province'), max_length=255)

	def __str__(self):
		return self.name

class Regencies(models.Model):
	province = models.ForeignKey(Provinces, verbose_name=_('Province'))
	name = models.CharField(verbose_name=_('Address'), max_length=255)

class Districts(models.Model):
	regency = models.ForeignKey(Regencies, verbose_name=_('Regency'))
	name = models.CharField(verbose_name=_('District'), max_length=255)

class Villages(models.Model):
	district = models.ForeignKey(Districts, verbose_name=_('District'))
	name = models.CharField(verbose_name=_('Village'), max_length=255)
