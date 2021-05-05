from django.contrib import admin
from Autoterra.models import  Bibliotheque, Affichage

#admin.site.register(Affichage)
#admin.site.register(Bibliotheque)

class AffichageAdmin(admin.ModelAdmin):
    pass
    list_display = ('Title','Humidite','Temperature')
    fields = ['Title','Humidite','Temperature']

admin.site.register(Affichage, AffichageAdmin)

class BibliothequeAdmin(admin.ModelAdmin):
    pass
    list_display = ('Animal','Image','Humidite_min','Humidite_max')
    fields = ['Animal','Image','Humidite_min','Humidite_max']

admin.site.register(Bibliotheque, BibliothequeAdmin)