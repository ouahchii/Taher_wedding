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
| `whatsapp` | numéro du bouton de secours, indicatif compris, sans `+` |
| `photo`    | image de fond du hero ; vide = silhouette dessinée |
| `ntfy`     | serveur de notification, `https://ntfy.sh` par défaut |
| `ntfyTopic`| nom du canal qui reçoit les réponses — à garder secret |

Le texte (basmala, prénoms, histoire, déroulé) se modifie directement dans le HTML.

## Recevoir les réponses (ntfy)

Le bouton « Envoyer ma réponse » publie la réponse sur un canal
[ntfy](https://ntfy.sh) ; la notification arrive sur le téléphone en une seconde.
Aucun compte, aucun serveur à héberger.

1. Installer l'application **ntfy** (Android, iOS) ou ouvrir `https://ntfy.sh/app`.
2. S'abonner au topic indiqué dans `ntfyTopic` (bloc `CONFIG` d'`index.html`).
3. Tester depuis un terminal :
   `curl -d "test" https://ntfy.sh/<le-topic>`

Le bouton « Envoyer par WhatsApp » reste disponible si la requête échoue
(réseau coupé, ntfy.sh bloqué).

> **Important** : sur le serveur public `ntfy.sh`, un topic n'est pas protégé par
> mot de passe. Quiconque connaît son nom peut lire les réponses. Le nom
> aléatoire fourni est la protection ; ne le publiez nulle part. Pour un vrai
> contrôle d'accès, hébergez votre propre serveur ntfy et renseignez son
> adresse dans `ntfy`.

## Contenu

- `index.html` — page complète : styles, scripts, silhouette et enveloppe SVG
- `assets/envelope.mp4` — animation d'ouverture (2 s)
- `assets/envelope-poster.jpg` — première image, affichée avant lecture

## Notes techniques

- Polices chargées depuis Google Fonts : Amiri, Cormorant Garamond, Josefin Sans
- Musique générée par l'API Web Audio, aucun fichier audio
- Réponses transmises à ntfy par `fetch`, WhatsApp (`wa.me`) en secours
- Animation d'ouverture muette : condition imposée par les navigateurs mobiles

Créé par Issam Ouahchi
