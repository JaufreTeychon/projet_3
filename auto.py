# Automatisation de la récupération des données

import pandas as pd
import warnings
warnings.filterwarnings ('ignore')
from datetime import datetime , timedelta
import requests 

# Définition du format des dates
format_date = "%Y-%m-%d"

# Obtenir la date actuelle
date_actuelle = datetime.now().strftime(format_date)

# URL des fichiers
url_logs_vols = f"http://sc-e.fr/docs/logs_vols_{date_actuelle}.csv"
url_degradations = f"http://sc-e.fr/docs/degradations_{date_actuelle}.csv"

# Téléchargement des fichiers
response_logs_vols = requests.get(url_logs_vols)
response_degradations = requests.get(url_degradations)

# Vérification des statuts de téléchargement
if response_logs_vols.status_code == 200:
    with open(f"logs_vols_{date_actuelle}.csv", "wb") as f:
         f.write(response_logs_vols.content)
    print("Logs vols téléchargés avec succès.")
else:
    print(f"Erreur lors du téléchargement des logs vols. Code de statut : {response_logs_vols.status_code}")

if response_degradations.status_code == 200:
    with open(f"degradations_{date_actuelle}.csv", "wb") as f:
        f.write(response_degradations.content)
    print("Dégradations téléchargées avec succès.")
else:
    print(f"Erreur lors du téléchargement des dégradations. Code de statut : {response_degradations.status_code}")
