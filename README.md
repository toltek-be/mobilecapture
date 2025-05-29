# Screenshot Capture (Mobile Portrait)

Ce projet permet de capturer automatiquement des **captures d’écran en mode portrait** d’une page web sur une cinquantaine de résolutions correspondant à des **smartphones réels** (iPhone, Galaxy, Pixel, etc.), le tout dans un environnement **Dockerisé avec Chrome Headless**.

---

## Fonctionnalités

- Capture **complète de la page** (scroll compris)
- Résolutions de plus de **50 modèles de smartphones**
- Affichage des dimensions + modèle dans le nom de fichier
- Dockerisé (aucune installation de Chrome ou WebDriver nécessaire)
- Personnalisation via variables d’environnement :
  - `TARGET_URL`: URL cible à capturer
  - `LOAD_DELAY`: délai d’attente avant capture (en secondes, par défaut `3`)

---

## Structure du projet

```txt
screencapture/
├── .gitignore
├── Dockerfile              # Image Docker avec Chrome + Selenium
├── requirements.txt        # Dépendances Python (Selenium)
├── script.py               # Script de capture
├── screenshots/            # Dossier où sont enregistrées les captures
└── run.sh                  # Script shell de lancement pratique

````

---

## Utilisation avec Docker 🐳 

### 1. Construire l’image Docker

```bash
#linux / macintel
docker build -t screencapture .
#mac puces arm 
docker build --platform=linux/amd64 -t screencapture .
````

### 2. Lancer la capture

```bash
docker run --rm \
  -e TARGET_URL="https://example.com" \
  -e LOAD_DELAY=3 \
  -v $(pwd)/screenshots:/screenshots \
  screencapture
```

Les captures sont enregistrées dans `./screenshots/`, nommées sous la forme :

```
screenshot_iPhone_12_390x2940.png
```

---

## Script de lancement rapide

```bash
./run.sh https://example.com 5
# Paramètres :
# `$1` → URL
# `$2` → Délai avant capture (optionnel, défaut = `3`)
```



---

## Personnalisation

Ajouter/supprimer des résolutions dans `script.py` :

```python
resolutions = [
    (375, 812, "iPhone_X"),
    (414, 896, "iPhone_XR"),
    etc…
]
```

Chaque tuple est de la forme : `(largeur, hauteur, nom_du_modele)`

---

## Dépendances

Les dépendances sont installées automatiquement via requirements.txt



---

## Pré-requis

* Docker 
* Dossier `screenshots/` pour stocker les images 

---

##  Licence

Ce projet est libre d'utilisation pour vos tests, rapports, automatisations ou audits visuels.



