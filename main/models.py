from __future__ import unicode_literals
from django.db import models
from housing.local_settings import local_GoogleAPI_key
from django.core.urlresolvers import reverse

import googlemaps

class GameStore(models.Model):
	name = models.CharField(max_length=70)
	address = models.CharField(max_length=150)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	website = models.CharField(max_length=70, null=True, blank=True)
	phone_number = models.CharField(max_length=20, null=True, blank=True)


	def __unicode__(self):
		return self.name






