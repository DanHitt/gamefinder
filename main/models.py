from __future__ import unicode_literals
from django.db import models
from gamefinder.local_settings import local_GoogleAPI_key
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from gamefinder.local_settings import local_GoogleAPI_key
import googlemaps



class Player(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_name = models.CharField(max_length=70)
	# icon 
	fname = models.CharField(max_length=70, null=True, blank=True)
	lname = models.CharField(max_length=70, null=True, blank=True)
	
	email = models.EmailField(max_length=254, null=True, blank=True)
	contact_info = models.CharField(max_length=70, null=True, blank=True)
	favorite_game = models.CharField(max_length=70, null=True, blank=True)

	MALE = 'M'
	FEMALE = 'F'
	OTHER = 'Other'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(OTHER, 'Other'),
		)
	sex = models.CharField(max_length=5, choices=GENDER_CHOICES, default=MALE)


	def __unicode__(self):
		return self.user_name


	def save(self):


		self.user.groups.add(Group.objects.get(name='Players')) #auto add group(Players) to all new users
		super(Player, self).save()


class GameStore(models.Model):
	name = models.CharField(max_length=70)
	store_hours = models.CharField(max_length=70, null=True, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	full_address = models.CharField(max_length=50, blank=True, editable=False)
	latitude = models.FloatField(null=True, blank=True, editable=False)
	longitude = models.FloatField(null=True, blank=True, editable=False)
	website = models.CharField(max_length=70, null=True, blank=True)
	facebook = models.CharField(max_length=70, null=True, blank=True)
	phone_number = models.CharField(max_length=20, null=True, blank=True)



	def __unicode__(self):
		return self.name

	def save(self):
	
		full_address = "%s %s %s %s %s" % (self.address,self.city,self.state,self.zipcode," USA")
		self.full_address = full_address

		gmaps = googlemaps.Client(key=local_GoogleAPI_key)
		latlng = gmaps.geocode(full_address)

		self.latitude = latlng[0]['geometry']['location']['lat'] 
		self.longitude = latlng[0]['geometry']['location']['lng'] 


		super(GameStore, self).save()



class Session(models.Model):
	name = models.CharField(max_length=70)
	contact_info = models.CharField(max_length=70, null=True, blank=True)
	game = models.CharField(max_length=70)
	needed_players = models.IntegerField()
	experience_range = models.CharField(max_length=70, default="any")
	date_created = models.DateField(auto_now=True)
	datetime_of_game = models.DateTimeField()
	description = models.CharField(max_length=70, null=True, blank=True)
	interested_players = models.ManyToManyField(Player)
	game_store = models.ForeignKey(GameStore)

	def __unicode__(self):
		return self.name 





