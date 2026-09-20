# -*- coding: utf-8 -*-
"""Fabrique la vignette de partage à partir de la carte.

Les réseaux sociaux attendent une image large (1200×630) ; la carte est un
portrait 9/16. On y découpe donc une bande horizontale centrée sur le sceau,
qui en est le point d'intérêt, puis on l'agrandit.

    python tools/make-og-image.py
"""
from PIL import Image

SOURCE = 'assets/card.jpg'
SORTIE = 'assets/og-image.jpg'
LARGEUR, HAUTEUR = 1200, 630

# Le sceau de cire est centré horizontalement, un peu sous la moitié de la carte.
CENTRE_SCEAU = 0.496   # en proportion de la hauteur


def fabriquer(source=SOURCE, sortie=SORTIE):
    carte = Image.open(source)
    l, h = carte.size

    bande = l * HAUTEUR / LARGEUR          # hauteur de bande au ratio voulu
    centre = h * CENTRE_SCEAU
    haut = max(0, min(h - bande, centre - bande / 2))

    vignette = carte.crop((0, int(haut), l, int(haut + bande)))
    vignette = vignette.resize((LARGEUR, HAUTEUR), Image.LANCZOS)
    vignette.save(sortie, 'JPEG', quality=88, optimize=True, progressive=True)

    import os
    print('%s : %d×%d, %.1f Ko' % (sortie, LARGEUR, HAUTEUR,
                                   os.path.getsize(sortie) / 1024))
    return sortie


if __name__ == '__main__':
    fabriquer()
