import requests
import random
import os
import tkinter as tk
from tkinter import ttk
import glob
import vdf

# ======================================
# CONFIG
# ======================================

API_KEY = ""
STEAM_ID = ""

STEAM_PATHS = [
    r"C:\Program Files (x86)\Steam\steamapps",
]

# ======================================
# RECUPERATION JEUX API
# ======================================

url = (
    "https://api.steampowered.com/"
    "IPlayerService/GetOwnedGames/v0001/"
)

params = {
    "key": API_KEY,
    "steamid": STEAM_ID,
    "format": "json",
    "include_appinfo": True
}

response = requests.get(url, params=params)
data = response.json()

games = data["response"]["games"]

# Tous les jeux
jeux = {}

for game in games:
    nom = game["name"]
    appid = str(game["appid"])

    jeux[nom] = {
        "appid": appid,
        "lien": f"steam://run/{appid}"
    }

# ======================================
# RECUPERATION JEUX INSTALLES
# ======================================

installed_ids = set()

manifest_files = []
for path in STEAM_PATHS:
    manifest_files += glob.glob(os.path.join(path, "appmanifest_*.acf"))

for file in manifest_files:
    try:
        data = vdf.load(open(file, encoding="utf-8"))
        appid = data["AppState"]["appid"]

        installed_ids.add(appid)

    except:
        pass

# ======================================
# VARIABLES
# ======================================

jeu_selectionne = None

# ======================================
# CHOIX ALEATOIRE
# ======================================

def choisir_jeu():
    global jeu_selectionne

    # Checkbox activée ?
    installed_only = var_installed.get()

    # Filtrage
    liste = []

    for nom, info in jeux.items():

        if installed_only:
            if info["appid"] in installed_ids:
                liste.append(nom)
        else:
            liste.append(nom)

    if not liste:
        label_resultat.config(
            text="Aucun jeu installé trouvé",
            fg="red"
        )
        return

    # Animation
    for _ in range(20):
        temp = random.choice(liste)

        label_resultat.config(text=temp)

        fenetre.update()
        fenetre.after(50)

    jeu_selectionne = random.choice(liste)

    label_resultat.config(
        text=f"🎮 {jeu_selectionne}",
        fg="green"
    )

# ======================================
# LANCER JEU
# ======================================

def lancer_jeu():
    if jeu_selectionne:
        os.startfile(jeux[jeu_selectionne]["lien"])

# ======================================
# INTERFACE
# ======================================

fenetre = tk.Tk()
fenetre.title("Steam Random Game")
fenetre.geometry("550x350")

titre = tk.Label(
    fenetre,
    text="🎲 Steam Random Game",
    font=("Arial", 22, "bold")
)
titre.pack(pady=20)

label_resultat = tk.Label(
    fenetre,
    text="Clique sur le bouton",
    font=("Arial", 16)
)
label_resultat.pack(pady=30)

# Checkbox
var_installed = tk.BooleanVar()

checkbox = tk.Checkbutton(
    fenetre,
    text="Jeux installés uniquement",
    variable=var_installed,
    font=("Arial", 12)
)

checkbox.pack(pady=10)

# Bouton random
btn_random = ttk.Button(
    fenetre,
    text="Choisir un jeu",
    command=choisir_jeu
)

btn_random.pack(pady=10)

# Bouton launch
btn_launch = ttk.Button(
    fenetre,
    text="Lancer le jeu",
    command=lancer_jeu
)

btn_launch.pack(pady=10)

fenetre.mainloop()