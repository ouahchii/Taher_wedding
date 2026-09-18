# Invitation — Taher & Samar

Invitation de mariage, page unique, sans dépendance à installer.
1er novembre 2026, Salle La Marquise, Sousse.

## Mise en ligne (GitHub Pages)

1. Créer un dépôt et y déposer ces fichiers à la racine.
2. Settings → Pages → Source : `Deploy from a branch`, branche `main`, dossier `/ (root)`.
3. L'adresse `https://<utilisateur>.github.io/<dépôt>/` est active après une minute.

## Ce qu'il faut modifier

Tout est regroupé dans le bloc `CONFIG`, en bas de `index.html` :

| champ      | rôle                                              |
|------------|---------------------------------------------------|
| `maries`   | noms affichés dans le message de réponse           |
| `dateISO`  | date et heure, utilisée par le compte à rebours    |
| `finISO`   | fin de la soirée, pour le lien agenda              |
| `lieu`     | adresse, utilisée par le lien Google Maps          |
| `whatsapp` | numéro qui reçoit les réponses, indicatif compris, sans `+` |
| `photo`    | image de fond du hero ; vide = silhouette dessinée |

Le texte (basmala, prénoms, histoire, déroulé) se modifie directement dans le HTML.

## Contenu

- `index.html` — page complète : styles, scripts, silhouette et enveloppe SVG
- `assets/envelope.mp4` — animation d'ouverture (2 s)
- `assets/envelope-poster.jpg` — première image, affichée avant lecture

## Notes techniques

- Polices chargées depuis Google Fonts : Amiri, Cormorant Garamond, Josefin Sans
- Musique générée par l'API Web Audio, aucun fichier audio
- Réponses transmises par lien `wa.me`, aucun serveur nécessaire
- Animation d'ouverture muette : condition imposée par les navigateurs mobiles

Créé par Issam Ouahchi
