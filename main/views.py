from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from itertools import chain

from .models import GameStore, Session, Player



def home(request):
	

	context = {}

	return render(request, 'index.html', context)

def base(request):
	

	context = {}

	return render(request, 'base.html', context)

def find_store_API(request):
	
	stores = GameStore.objects.all()
	sessions = Session.objects.all()
	joined_collection = list(chain(stores, sessions))

	json = serializers.serialize('json', joined_collection,)
	# complex_output = serializers.serialize('json', complexes, fields=('name', 'address'))
	# listings_output = serializers.serialize('json', listings, fields=('name', 'address', 'city', 'state'))

	output = json

	return HttpResponse(output, content_type='application/json')



def player_view_API(request):
	User = get_user_model()

	players = Player.objects.filter().only('id','user_name','contact_info')
	# players = Player.objects.all()


	# joined_collection = list(chain(player, joined_collection))

	json = serializers.serialize('json', players,)
	output = json

	return HttpResponse(output, content_type='application/json')

	# Now to Create User:
	# User.objects.create_user(username='user2', password='pass')
	# Remove User:
	# user_rem=User.objects.get(username='user2')
	# user_rem.is_active=False
	# user_rem.save()

	# autofixture string values 
	# ['Joe', 'Eddie', 'Samir', 'Josesph', 'Jose','amon8r', 'ethan8r' 'Jen', 'Fred', 'Raph', 'Faker', 'Yasuo', 'Timid', 'Jund', 'LSV', 'Chip']
	# ['dnd', 'd&d', 'D&D', 'Dungeons and Dragons', "Magic", "magic", 'magic the gathering', "Magic: The Gathering", 'warhammer', 'Warhammer', 'WH', 'warham', 'PathFinder', 'pathfinder', 'dungeon maker', 'Dungeon Maker']



