from gastenboek.models import Reactie
from django.contrib import admin

class ReactieAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['naam']}),
            ('Bericht',          {'fields': ['bericht']}),
            ('Publicatie datum', {'fields': ['datum']})
    ]

admin.site.register(Reactie, ReactieAdmin)