# Invitation — Taher & Samar

Invitation de mariage, page unique, en français, sans dépendance à installer.
1er novembre 2026, Salle La Marquise, Sousse.

## Mise en ligne (Netlify)

1. [app.netlify.com/start/repos](https://app.netlify.com/start/repos) → autoriser
   GitHub → choisir ce dépôt.
2. Build command : **vide**. Publish directory : **`.`** — `netlify.toml` les fixe
   déjà, l'interface doit simplement ne pas les contredire.
3. **Deploy**. Chaque `git push` sur `main` redéploie automatiquement.
4. *Site configuration → Forms → Form notifications* : ajouter une notification
   par e-mail. **Sans cela, les réponses n'arrivent que dans le tableau de bord.**

`netlify.toml` ne fait que deux choses : publier la racine, et mettre `assets/`
en cache long avec `index.html` en revalidation permanente, pour qu'une
correction soit visible tout de suite.

> Le site dépend désormais de Netlify pour la collecte des réponses. Sur un autre
> hébergeur, la page s'afficherait normalement mais le formulaire ne collecterait
> rien : c'est pourquoi `vercel.json` a été retiré plutôt que laissé en place.

## Ce qu'il faut modifier

Tout est regroupé dans le bloc `CONFIG`, en haut du script d'`index.html` :

| champ      | rôle                                                      |
|------------|-----------------------------------------------------------|
| `dateISO`  | date et heure, utilisée par le compte à rebours            |
| `lieu`     | adresse, utilisée par le lien Google Maps                  |
| `photo`    | image de fond du hero ; vide = silhouette dessinée         |

Adresse en ligne : <https://taher-samar-wedding.netlify.app/>

Les métadonnées de partage (`og:url`, `og:image`, `canonical`) contiennent ce
domaine **en dur** : si le site est renommé, il faut les reprendre dans le
`<head>` d'`index.html`, faute de quoi l'aperçu des liens cassera.

## Recevoir les réponses (Netlify Forms)

Le formulaire de réponse est un vrai `<form name="rsvp" data-netlify="true">`.
Netlify le repère **en analysant le HTML au moment du déploiement** : il doit
donc rester écrit en dur dans la page, jamais construit en JavaScript.

Les réponses arrivent dans *Site configuration → Forms*, et par e-mail si la
notification est configurée. Champs transmis : `presence` (`oui` / `peut` / `non`), `nom`, `nb` et `mot`.

L'envoi se fait en arrière-plan (`fetch` vers `/`), pour que l'invité reste sur
l'invitation au lieu d'atterrir sur l'accusé de réception de Netlify. Le champ
`bot-field`, caché, sert d'appât anti-spam.

> ⚠️ Le forfait gratuit plafonne à **100 réponses par mois**. Les réponses d'un
> mariage se concentrent sur les semaines qui précèdent : surveillez le compteur
> à l'approche de la date, quitte à passer au forfait payant ce mois-là.

En local, l'envoi échoue forcément : `POST /` n'existe que sur Netlify.

## Contenu

- `index.html` — page complète : styles, scripts, silhouette SVG
- `assets/card.jpg` — la carte fermée, fendue en deux battants à l'ouverture
- `assets/og-image.jpg` — vignette 1200×630 pour l'aperçu des liens partagés
- `tools/extract-card.py` — script qui a extrait `card.jpg` d'`index_nour.html`
- `tools/make-og-image.py` — script qui recadre `card.jpg` en vignette
- `netlify.toml` — publication et en-têtes de cache
- `.nojekyll` — pour GitHub Pages

## Notes techniques

- Polices chargées depuis Google Fonts : Cormorant Garamond, Josefin Sans
- Musique générée par l'API Web Audio, aucun fichier audio
- Réponses collectées par Netlify Forms, sans serveur à héberger
- Ouverture : la carte se fend en deux battants (`rotateY` sur ses deux moitiés),
  pendant que la pièce s'assombrit et que deux barres descendent en letterbox
- Le verrou de défilement double `overflow:hidden` d'un blocage de `wheel` et
  `touchmove` : Safari mobile laisse défiler au doigt sans cela

Créé par Issam Ouahchi
