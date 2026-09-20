# -*- coding: utf-8 -*-
"""Extrait une image encodée en base64 depuis index_nour.html vers un fichier.

index_nour.html — la maquette anglaise d'où provient l'ouverture en deux
battants — embarque ses images dans des propriétés CSS personnalisées :

    --card-img: url("data:image/jpeg;base64,/9j/4AAQ...")

Ce script isole l'une d'elles et l'écrit sur disque, pour que l'origine de
assets/card.jpg reste traçable.

    python tools/extract-card.py card-img assets/card.jpg
"""
import base64
import io
import os
import re
import sys

SOURCE = 'index_nour.html'


def extraire(variable, destination, source=SOURCE):
    html = io.open(source, encoding='utf-8').read()
    motif = r'--%s:\s*url\(\s*"?data:image/(\w+);base64,([^")]+)' % re.escape(variable)
    trouve = re.search(motif, html)
    if not trouve:
        raise SystemExit("--%s introuvable dans %s" % (variable, source))

    fmt, donnees = trouve.group(1), trouve.group(2)
    binaire = base64.b64decode(donnees)

    dossier = os.path.dirname(destination)
    if dossier and not os.path.isdir(dossier):
        os.makedirs(dossier)
    with open(destination, 'wb') as f:
        f.write(binaire)

    print("--%s (%s) -> %s : %.1f Ko (%.1f Ko en base64)"
          % (variable, fmt, destination, len(binaire) / 1024, len(donnees) / 1024))
    return destination


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("usage: python tools/extract-card.py <variable> <destination>")
    extraire(sys.argv[1], sys.argv[2])
