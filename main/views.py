from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

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


	player = Player.objects.all()
	# joined_collection = list(chain(player, joined_collection))

	json = serializers.serialize('json', player,)
	output = json

	return HttpResponse(output, content_type='application/json')


