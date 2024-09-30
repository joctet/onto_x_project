import csv

def parse_csv(file_path):
    '''
    Parse le fichier csv.
    
    Arguments : 
    file_path (str): Le chemin vers le fichier CSV contenant les entités.
    
    Returns : 
    entities (dict) : Un dictionnaire où les clés sont les 'Class ID' et 
    les valeurs sont les labels et les parents des entités.
    '''
    entities = {}
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        # print(csv_reader)
        for row in csv_reader:
            class_id = row['Class ID']
            preferred_label = row['Preferred Label']
            parents = row['Parents'].split('|') if row['Parents'] else []

            # On sauvegarde les infos de chaque entité dans un dictionnaire
            entities[class_id] = {
                'preferred_label': preferred_label,
                'parents': parents
            }
    return entities