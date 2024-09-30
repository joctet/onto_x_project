def get_ancestors_and_siblings(entities, entity_id, current_depth=0, results=None):
    """
    Récupère les ancêtres directs et indirects ainsi que les "frères et sœurs" d'une entité
    avec leur profondeur.

    Args:
    entities (dict): Un dictionnaire contenant toutes les entités avec leurs parents.
    entity_id (str): L'ID de l'entité pour laquelle on veut récupérer les ancêtres et frères/sœurs.
    current_depth (int): La profondeur actuelle (0 pour les frères/sœurs, 1 pour les parents, etc.).
    results (dict): Un dictionnaire accumulant les ancêtres et leur profondeur.

    Returns:
    dict: Un dictionnaire avec les ancêtres et frères/sœurs de l'entité donnée, où les clés 
    sont les labels des entités et les valeurs sont les profondeurs dans la hiérarchie.
    - Les frères et sœurs (pathologies ayant le même parent) ont une profondeur de 0.
    - Les parents directs ont une profondeur de 1.
    - Les parents des parents ont une profondeur de 2.
    - et ainsi de suite.
    """
    if results is None:
        results = {}

    entity = entities.get(entity_id, {})
    label = entity.get('preferred_label')
    
    parents = entity.get('parents', [])

    
    if current_depth == 0 :
    # Ajouter les frères et sœurs à la profondeur 0 pour la génération actuelle
    
        for parent_id in parents:
            siblings = get_siblings(entities, parent_id)
            
            for sibling in siblings:
                if sibling['preferred_label'] not in results:
                    results[sibling['preferred_label']] = current_depth  # Profondeur actuelle pour les frères/sœurs
        
            # On ajoute le parent à la profondeur actuelle + 1
            parent = entities.get(parent_id, {})
            parent_label = parent.get('preferred_label')
            if parent_label and parent_label not in results:
                results[parent_label] = current_depth + 1

            # Ajouter les ancêtres à profondeur actuelle + 1 (grands-parents et plus)
            get_ancestors_and_siblings(entities, parent_id, current_depth + 1, results)
    
    else :

        for parent_id in parents:
            # On ajoute le parent à la profondeur actuelle + 1
            parent = entities.get(parent_id, {})
            parent_label = parent.get('preferred_label')
            if parent_label and parent_label not in results:
                results[parent_label] = current_depth + 1

            # Ajouter les ancêtres à profondeur actuelle + 1 (grands-parents et plus)
            get_ancestors_and_siblings(entities, parent_id, current_depth + 1, results)

    return results


def get_siblings(entities, parent_id):
    """
    Récupère les "frères et sœurs" d'une entité, c'est-à-dire les autres enfants d'un parent donné.
    Args:
    entities (dict): Le dictionnaire des entités.
    parent_id (str): L'ID du parent dont on cherche les enfants.

    Returns:
    list: Une liste des entités qui partagent le même parent.
    """
    siblings = []
    for entity_id, entity_data in entities.items():
        if parent_id in entities[entity_id]["parents"]:
            siblings.append(entity_data)
    return siblings