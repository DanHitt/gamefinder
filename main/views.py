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
	# joined_collection = list(chain(complexes, listings))r

	json = serializers.serialize('json', stores,)
	# complex_output = serializers.serialize('json', complexes, fields=('name', 'address'))
	# listings_output = serializers.serialize('json', listings, fields=('name', 'address', 'city', 'state'))

	output = json

	return HttpResponse(output, content_type='application/json')


def store_detail_view_API(request, pk):
	request.method == 'POST'

	game_store = GameStore.objects.get(pk=pk)
	sessions = Session.objects.filter(game_store=pk)
	# players = sessions.interested_players
	print sessions
	print "______"

	print"8888"
	print sessions
	json = serializers.serialize('json', sessions,)
	output = json

	return HttpResponse(output, content_type='application/json')


def interested_player_view_API(request, players):

	print players
	print"----first----"
	string = []
	for x in (range(len(players))):
		print players[x:x+1]
		print "*"
		print x
		string.extend(players[x:x+1])
	players = string
	print"----"
	print players
	joined_collection = {}
	for player in players:
		player = Players.objects.get(interested_players=player)
		joined_collection = list(chain(player, joined_collection))


	print"8888"
	print joined_collection
	json = serializers.serialize('json', joined_collection,)
	output = json

	return HttpResponse(output, content_type='application/json')


