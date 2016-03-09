from django.contrib import admin

from .models import Player, Session, GameStore


admin.site.register(Player)
admin.site.register(Session)
admin.site.register(GameStore)

