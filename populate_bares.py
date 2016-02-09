import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dai_django_project.settings')

import django
django.setup()

from bares.models import Bares, Tapas


def populate():
    krisis_nom = add_bar("Krisis", "Camino de Ronda", 5)

    add_tapa(bar=krisis_nom,
        nom="Croquetas",
        vot=2)

    add_tapa(bar=krisis_nom,
        nom="Hamburguesa con queso",
        vot=1)

    add_tapa(bar=krisis_nom,
        nom="Pinchito",
        vot=4)

    bubion_nom = add_bar("Bubion", "Calle Socrates", 2)

    add_tapa(bar=bubion_nom,
        nom="Lomo con roquefort",
        vot=0)

    add_tapa(bar=bubion_nom,
        nom="Hamburguesa con huevo",
        vot=1)

    add_tapa(bar=bubion_nom,
        nom="Pollo con limon",
        vot=4)

    asturcon_nom = add_bar("Asturcon", "Glorieta de Arabial", 3)

    add_tapa(bar=asturcon_nom,
        nom="Lomo con queso",
        vot=1)

    add_tapa(bar=asturcon_nom,
        nom="Hamburguesa",
        vot=2)

    # Print out what we have added to the user.
    for c in Bares.objects.all():
        for p in Tapas.objects.filter(n_bar=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_tapa(bar, nom, vot):
    p = Tapas.objects.get_or_create(n_bar=bar,nombre=nom, votos=vot)[0]
    p.save()
    return p

def add_bar(nomb, dire, voto):
    c = Bares.objects.get_or_create(n_bar=nomb)[0]
    c.direccion = dire
    c.votos = voto
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Bares population script..."
    populate()