import streamlit as st
import requests
from urllib.parse import quote  # Importer quote pour encoder l'URL

# URL de l'API FastAPI
API_URL = "http://localhost:8000/entity"

# Titre de l'application
st.title("Entity Hierarchy Search")

# Section de documentation utilisateur
st.markdown("""
## Comment utiliser cette APLI ?

1. Entrez l'**ID de l'entité** que vous souhaitez interroger dans le champ de texte.
   - Exemple d'ID : `http://entity/CST/CERVIX%20DIS`
2. Cliquez sur le bouton **"Search Hierarchy"** pour lancer la recherche.
3. Les résultats de la hiérarchie s'afficheront sous forme de liste indiquant chaque relation et sa profondeur dans la hiérarchie.

L'API utilise un fichier CSV pour reconstruire la hiérarchie des entités, et les résultats affichés montrent les relations entre l'entité recherchée et d'autres entités associées.
""")

# Champ pour entrer l'ID de l'entité, avec un exemple par défaut
entity_id = st.text_input("Enter Entity ID", placeholder="http://entity/CST/CERVIX%20DIS")

# Bouton pour lancer la recherche
if st.button("Search Hierarchy"):
    # Vérifier que l'ID de l'entité n'est pas vide
    if entity_id:

        # Encodage de l'URL avec urllib pour gérer les caractères spéciaux
        encoded_entity_id = quote(entity_id, safe=':/')  # ici on garde ":" et "/"
        
        # Appel de l'API FastAPI avec l'ID encodé
        response = requests.get(f"{API_URL}?entity_id={encoded_entity_id}")
        
        # Vérification de la réussite de la requête
        if response.status_code == 200:
            hierarchy = response.json()  # On récupére la réponse JSON
            
            # Affichage des résultats de la hiérarchie
            st.write(f"Hierarchy for entity: {entity_id}")
            for relation, depth in hierarchy.items():
                st.write(f"{relation}: Depth {depth}")
        else:
            st.error(f"Entity not found or error: {response.status_code}")
    else:
        st.warning("Please enter a valid entity ID")




# import streamlit as st
# import requests

# # L'URL de ton API FastAPI
# API_URL = "http://localhost:8000/entity"

# # Titre de l'application
# st.title("Entity Hierarchy Search")

# # Champ de texte pour entrer l'ID de l'entité
# entity_id = st.text_input("Enter Entity ID", placeholder="http://entity/CST/CERVIX%20DIS")

# # Bouton pour lancer la recherche
# if st.button("Search Hierarchy"):
#     # Vérifier que l'ID de l'entité n'est pas vide
#     if entity_id:
#         # Appeler l'API FastAPI
#         response = requests.get(f"{API_URL}/{entity_id}")
        
#         # Vérifier si la requête a réussi
#         if response.status_code == 200:
#             hierarchy = response.json()  # Récupérer la réponse JSON
            
#             # Afficher les résultats de la hiérarchie
#             st.write(f"Hierarchy for entity: {entity_id}")
#             for relation, depth in hierarchy.items():
#                 st.write(f"{relation}: Depth {depth}")
#         else:
#             st.error(f"Entity not found or error: {response.status_code}")
#     else:
#         st.warning("Please enter a valid entity ID")