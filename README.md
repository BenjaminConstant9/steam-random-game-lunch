# :video_game: Steam Random Game Launcher

Un script Python qui permet de lancer automatiquement un jeu aléatoire depuis votre bibliothèque Steam.

Le script récupère vos jeux via l’API Steam, sélectionne un jeu aléatoire parmi ceux que vous possédez, puis le lance directement sur votre PC.

---

# :rocket: Objectif

Le but de ce projet est simple :

- récupérer la liste de vos jeux Steam ;
- choisir un jeu aléatoire ;
- lancer automatiquement ce jeu depuis votre installation Steam.

Pratique si vous ne savez jamais à quoi jouer ou si vous voulez redécouvrir des jeux oubliés de votre bibliothèque.

---

# :package: Installation

## Prérequis

- Python 3.12
- Steam installé sur votre PC

## Installation des dépendances

Clonez le repository :

```bash
git clone <URL_DU_REPOSITORY>
cd <NOM_DU_PROJET>

---

# ⚙️ Configuration

Avant de lancer le script, vous devez configurer plusieurs informations importantes.

## 1. Clé API Steam

Récupérez votre clé API Steam ici :

👉 https://steamcommunity.com/dev/apikey

Puis renseignez-la dans le script :

python
API_KEY = ""

---

## 2. Steam ID

Récupérez votre Steam ID ici :

👉 https://steamid.io/

Puis ajoutez-le dans le script :

```python
STEAM_ID = "76561198267777638"
```

---

## 3. Chemin Steam

Vous devez également renseigner le chemin vers votre dossier `steamapps`.

Le fichier `libraryfolders.vdf` doit être présent dans ce dossier.

Exemple :

```python
STEAM_PATHS = [
    r"C:\Program Files (x86)\Steam\steamapps",
]
```

---

# ▶️ Utilisation

Lancez simplement le script :

```bash
python steam_random_game.py
```

Le programme :

1. récupère vos jeux Steam ;
2. choisit un jeu aléatoire ;
3. lance automatiquement le jeu.

---

# 🛠️ Technologies utilisées

- Python 3.12
- API Steam Web
- Steam Local Library Detection

---

# 📌 Notes

- Le compte Steam doit être public pour récupérer les jeux via l’API.
- Steam doit être installé et connecté.
- Vérifiez que les chemins renseignés dans `STEAM_PATHS` sont corrects.
