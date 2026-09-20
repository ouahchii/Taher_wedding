# Invitation — Taher & Samar

Invitation de mariage, page unique, sans dépendance à installer.
1er novembre 2026, Salle La Marquise, Sousse.
Bilingue : **arabe par défaut**, français accessible d'un bouton.

## Mise en ligne

### Vercel (recommandé)

1. [vercel.com/new](https://vercel.com/new) → **Import Git Repository** → choisir ce dépôt.
2. Framework Preset : **Other**. Build Command et Output Directory : laisser vides.
3. **Deploy**. Chaque `git push` sur `main` redéploie automatiquement.

`vercel.json` ne fait qu'une chose : mettre `assets/` en cache long et `index.html`
en revalidation permanente, pour qu'une correction soit visible tout de suite.

### GitHub Pages

Settings → Pages → Source : `Deploy from a branch`, branche `main`, dossier `/ (root)`.
L'adresse `https://<utilisateur>.github.io/<dépôt>/` est active après une minute.
Le fichier `.nojekyll` est déjà là ; `vercel.json` y est simplement ignoré.

## Ce qu'il faut modifier

Tout est regroupé dans le bloc `CONFIG`, en haut du script d'`index.html` :

| champ      | rôle                                                      |
|------------|-----------------------------------------------------------|
| `maries`   | noms latins, repris dans le message de réponse français    |
| `mariesAr` | noms arabes, repris dans le message de réponse arabe       |
| `dateISO`  | date et heure, utilisée par le compte à rebours            |
| `finISO`   | fin de la soirée, pour le lien agenda                      |
| `lieu`     | adresse, utilisée par le lien Google Maps                  |
| `whatsapp` | numéro qui reçoit les réponses, indicatif compris, sans `+`|
| `photo`    | image de fond du hero ; vide = silhouette dessinée         |

> ⚠️ `whatsapp` vaut encore `21600000000`, un numéro de démonstration.
> **À remplacer avant de diffuser le lien**, sinon les réponses ne partent nulle part.

## Les deux langues

L'**arabe est écrit directement dans le HTML** : c'est ce que voit l'invité même si
le JavaScript échoue. Le français vit dans l'objet `FR` du script, et le bouton
en bas à gauche bascule d'une langue à l'autre (choix retenu par `localStorage`).

Pour modifier un texte, il faut donc le changer **aux deux endroits** :

- l'arabe dans la balise HTML, repérée par son attribut `data-t="clé"` ;
- le français à la même `clé` dans l'objet `FR`.

Les phrases construites par le script (messages d'erreur, contenu WhatsApp)
sont dans `TXT.fr` et `TXT.ar`. Les attributs `data-t-ph` et `data-t-aria` font
la même chose pour les textes indicatifs des champs et les libellés d'accessibilité.

Côté mise en forme, le bloc CSS `html[lang="ar"]` annule les interlettrages,
les majuscules et les italiques du thème latin : appliqués à l'arabe, ils
brisent la ligature des lettres ou produisent une fausse inclinaison.

## Contenu

- `index.html` — page complète : styles, scripts, silhouette et enveloppe SVG
- `assets/envelope.mp4` — animation d'ouverture (2 s)
- `assets/envelope-poster.jpg` — première image, affichée avant lecture
- `vercel.json` — en-têtes de cache
- `.nojekyll` — pour GitHub Pages

## Notes techniques

- Polices chargées depuis Google Fonts : Amiri (arabe), Cormorant Garamond, Josefin Sans
- Musique générée par l'API Web Audio, aucun fichier audio
- Réponses transmises par lien `wa.me`, dans la langue choisie par l'invité ; aucun serveur nécessaire
- Animation d'ouverture muette : condition imposée par les navigateurs mobiles

Créé par Issam Ouahchi
