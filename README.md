# 🎮 Steam Random Game Launcher

Un script Python qui lance automatiquement un jeu aléatoire depuis votre bibliothèque Steam.

Le programme :

- récupère vos jeux via l’API Steam ;
- choisit un jeu aléatoire ;
- lance automatiquement le jeu sur votre PC.

Idéal pour redécouvrir des jeux oubliés ou arrêter de passer 30 minutes à choisir quoi lancer.

---

## 🚀 Fonctionnalités

- 🎲 Sélection aléatoire d’un jeu Steam
- 📚 Récupération automatique de votre bibliothèque
- ▶️ Lancement automatique du jeu via Steam
- 🖥️ Détection des bibliothèques Steam locales

---

## 📦 Installation

### Prérequis

- Python 3.12
- Steam installé et connecté

### Cloner le projet

```bash
git clone <URL_DU_REPOSITORY>
cd <NOM_DU_PROJET>
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Avant de lancer le script, configurez les informations suivantes.

### 🔑 Clé API Steam

Récupérez votre clé API ici :

👉 https://steamcommunity.com/dev/apikey

Puis ajoutez-la dans le script :

```python
API_KEY = "VOTRE_CLE_API"
```

---

### 🆔 Steam ID

Récupérez votre Steam ID ici :

👉 https://steamid.io/

Puis ajoutez-le dans le script :

```python
STEAM_ID = "76561198267777638"
```

---

### 📁 Chemin de Steam

Indiquez le chemin vers votre dossier `steamapps`.

Le fichier `libraryfolders.vdf` doit être présent dans ce dossier.

Exemple :

```python
STEAM_PATHS = [
    r"C:\Program Files (x86)\Steam\steamapps",
]
```

---

## ▶️ Utilisation

Lancez simplement le script :

```bash
python steam_random_game.py
```

### Le programme va :

1. récupérer votre bibliothèque Steam ;
2. choisir un jeu aléatoire ;
3. lancer automatiquement le jeu sélectionné.

---

## 🛠️ Technologies utilisées

- Python 3.12
- API Steam Web
- Gestion des bibliothèques Steam locales

---

## 📌 Notes importantes

- Votre profil Steam doit être public pour permettre la récupération des jeux via l’API.
- Steam doit être installé et connecté.
- Vérifiez que les chemins définis dans `STEAM_PATHS` sont corrects.

---

## 📄 Licence

Ce projet est distribué sous licence MIT.
