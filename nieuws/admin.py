from nieuws.models import Artikel
from django.contrib import admin

class ArtikelAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['titel']}),
            ('Bericht',          {'fields': ['bericht']}),
            ('Gepubliceerd op',  {'fields': ['datum']})
    ]
    list_display = ('datum', 'titel', 'bericht')
    # list_filter = ['datum']
    search_fields = ['titel', 'bericht']
    # date_hierarchy = 'datum'

admin.site.register(Artikel, ArtikelAdmin)