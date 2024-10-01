import os
from fastapi import FastAPI, Request
from urllib.parse import unquote
from .parse import parse_csv
from .hierarchie import get_ancestors_and_siblings

app = FastAPI()

# on charge le csv au démarrage
# print(os.getcwd())
csv_path = os.path.join("data", "onto_x.csv")
entities = parse_csv(csv_path)

@app.get("/entity")
def get_entity_hierarchy(request: Request, entity_id: str):

    print(f"Requête pour l'entité ID: {entity_id}")

    # # quand on passe par streamlit le décodage est déja effectué
    # relationships = get_ancestors_and_siblings(entities, entity_id)

    # Décodage de l'entity_id (caractères spéciaux) avec urllib:
    decoded_entity_id = unquote(entity_id)
    # Remplacer les espaces par %20 pour corriger les ID incorrects
    corrected_entity_id = decoded_entity_id.replace(" ", "%20")
    
    # Logs : vérification de l'ID après correction
    print(f"Requête pour l'entité ID: {entity_id}")
    print(f"ID corrigé: {corrected_entity_id}")

    # Récupérer la hiérarchie pour l'entité donnée
    relationships = get_ancestors_and_siblings(entities, corrected_entity_id)
    
    # Retourner les relations hiérarchiques sous forme de JSON
    return relationships