import graphe
#outils de file
def nouvelle_file():
    return list()

def enfiler(f,e):
    f.append(e)

def defiler(f):
    return f.pop(0)

def file_vide(f): 
    return len(f) == 0

#outils de pile
def nouvelle_pile():
    return list()

def empiler(p, e):
    p.append(e)

def depiler(p):
    return p.pop()

def pile_vide(p):
    return len(p) == 0

def nombre_aretes_matrice(matrice):
    """
    Retourne le nombre d'arêtes dans un graphe non orienté
    représenté par une matrice d'adjacence.
    """
    nombre = 0
    for i in range(len(matrice)):
        for j in range(i, len(matrice)):  # Parcours uniquement la moitié supérieure
            if matrice[i][j] == 1:
                nombre += 1
    return nombre


def nombre_aretes_liste(liste_adjacence):
    """
    Retourne le nombre d'arêtes dans un graphe non orienté 
    représenté par une liste d'adjacence.
    """
    nombre = 0
    vus = set()  # Ensemble pour garder trace des arêtes déjà comptées

    for sommet, voisins in liste_adjacence.items():
        for voisin in voisins:
            # Vérifier si l'arête n'a pas déjà été comptée
            if (voisin, sommet) not in vus:
                nombre += 1
                vus.add((sommet, voisin))  # Ajouter l'arête dans l'ensemble des arêtes vues

    return nombre


#print(nombre_aretes_matrice(graphe.Mat))
#print(nombre_aretes_liste(graphe.Adj))

def nombre_d_arcs_matrice(matrice_adjacence):
    """
    Calcule le nombre d'arcs dans un graphe représenté par une matrice d'adjacence.

    :param matrice_adjacence: Liste de listes représentant la matrice d'adjacence.
    :return: Nombre total d'arcs dans le graphe.
    """
    return sum(sum(ligne) for ligne in matrice_adjacence)

def nombre_d_arcs_liste(liste_adjacence):
    """
    Calcule le nombre d'arcs dans un graphe représenté par une liste d'adjacence.

    :param liste_adjacence: Dictionnaire ou liste représentant la liste d'adjacence.
    :return: Nombre total d'arcs dans le graphe.
    """
    return sum(len(voisins) for voisins in liste_adjacence.values())

#print(nombre_d_arcs_matrice(graphe.Mat))
#print(nombre_d_arcs_liste(graphe.Adj))

def charger_graphe(fichier_texte, representation='matrice'):
    """
    Charge un graphe à partir d'un fichier texte et le représente en mémoire sous forme de matrice d'adjacence
    ou de liste d'adjacence.
    
    :param fichier_texte: Le fichier contenant la description du graphe.
    :param representation: 'matrice' pour matrice d'adjacence, 'liste' pour liste d'adjacence.
    :return: Tuple contenant la liste des sommets et la représentation du graphe.
    """
    # Lecture du fichier
    with open(fichier_texte, 'r') as f:
        lignes = f.readlines()

    # Récupération du type de graphe
    type_graphe = lignes[0].strip()

    # Récupération des sommets
    ns_lignes = int(lignes[1].split()[0])
    sommets = [lignes[i + 2].strip() for i in range(ns_lignes)]

    # Récupération des arcs ou arêtes
    na_lignes = int(lignes[ns_lignes + 2].split()[0])
    arcs_ou_aretes = [tuple(ligne.strip().split()) for ligne in lignes[ns_lignes + 3:ns_lignes + 3 + na_lignes]]

    # Génération de la représentation mémoire en fonction du type de graphe et du choix de représentation
    if type_graphe == "GRAPHE ORIENTE":
        return generer_graphe(sommets, arcs_ou_aretes, representation, orienté=True)
    elif type_graphe == "GRAPHE NON ORIENTE":
        return generer_graphe(sommets, arcs_ou_aretes, representation, orienté=False)
    else:
        raise ValueError("Type de graphe non valide. Choisissez 'GRAPHE ORIENTE' ou 'GRAPHE NON ORIENTE'.")

def generer_graphe(sommets, arcs_ou_aretes, representation, orienté):
    """
    Génère la représentation en fonction du type de graphe et de la représentation mémoire choisie (matrice ou liste).
    """
    if representation == 'matrice':
        return sommets, generer_matrice(sommets, arcs_ou_aretes, orienté)
    elif representation == 'liste':
        return sommets, generer_liste(sommets, arcs_ou_aretes, orienté)
    else:
        raise ValueError("Représentation non valide. Choisissez 'matrice' ou 'liste'.")

def generer_matrice(sommets, arcs_ou_aretes, orienté=bool):
    """
    Génère la matrice d'adjacence pour un graphe, orienté ou non.
    """
    ns_lignes = len(sommets)
    matrice = [[0] * ns_lignes for _ in range(ns_lignes)]
    for arc in arcs_ou_aretes:
        i = sommets.index(arc[0])
        j = sommets.index(arc[1])
        matrice[i][j] = 1
        if not orienté:
            matrice[j][i] = 1  # Graphe non orienté, ajout dans les deux sens
    return matrice

def generer_liste(sommets, arcs_ou_aretes, orienté=bool):
    """
    Génère la liste d'adjacence pour un graphe, orienté ou non.
    """
    liste_adj = {sommet: [] for sommet in sommets}
    for arc in arcs_ou_aretes:
        i = sommets.index(arc[0])
        j = sommets.index(arc[1])
        liste_adj[sommets[i]].append(sommets[j])
        if not orienté:
            liste_adj[sommets[j]].append(sommets[i])  # Graphe non orienté, ajout dans les deux sens
    return liste_adj

def parcours_largeur(matrice_adjacence, sommet_depart):
    """
    Effectue un parcours en largeur sur un graphe représenté par une matrice d'adjacence.

    :param matrice_adjacence: Liste de listes représentant la matrice d'adjacence.
    :param sommet_depart: Indice du sommet de départ (int).
    :return: Liste des sommets visités dans l'ordre du parcours en largeur.
    """
    res = []  # Liste des sommets explorés (résultat final)
    file = nouvelle_file()  
    vus = set()  

    enfiler(file, sommet_depart)
    vus.add(sommet_depart)

    # Parcours en largeur
    while not file_vide(file):
        courant = defiler(file)  
        res.append(courant) 

        # Parcourir les voisins du sommet courant
        for voisin, est_voisin in enumerate(matrice_adjacence[courant]):
            if est_voisin == 1 and voisin not in vus:
                vus.add(voisin)  # Marquer comme visité
                enfiler(file, voisin)  # Ajouter à la file des sommets à explorer

    return res

def parcours_profondeur(matrice_adjacence, sommet_depart):
    """
    Effectue un parcours en profondeur sur un graphe représenté par une matrice d'adjacence.

    :param matrice_adjacence: Liste de listes représentant la matrice d'adjacence.
    :param sommet_depart: Indice du sommet de départ (int).
    :return: Liste des sommets visités dans l'ordre du parcours en profondeur.
    """
    res = [] 
    pile = nouvelle_pile() 
    vus = set()

    empiler(pile, sommet_depart)
    vus.add(sommet_depart)

    # Parcours en profondeur
    while not pile_vide(pile):
        courant = depiler(pile)
        if courant not in res:
            res.append(courant)

        # Ajouter les voisins du sommet courant à la pile
        for voisin, est_voisin in enumerate(matrice_adjacence[courant]):
            if est_voisin == 1 and voisin not in vus:
                vus.add(voisin)
                empiler(pile, voisin)

    return res

def reseau_une_seule_communaute(matrice_adjacence):

    # Utiliser la fonction parcours_largeur pour visiter les sommets
    sommets_visites = parcours_largeur(matrice_adjacence, 0)
    
    # Si tous les sommets ont été visités, il s'agit d'une seule communauté
    return len(sommets_visites) == len(matrice_adjacence)

def lire_graphe(chemin_fichier):
    """
    Lit un fichier décrivant un graphe et retourne une liste d'adjacence.

    :param chemin_fichier: Chemin du fichier contenant le graphe.
    :return: Liste d'adjacence (dictionnaire).
    """
    graphe = {}
    try:
        with open(chemin_fichier, 'r') as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                
                # Ignorer les lignes vides ou les métadonnées
                if not ligne or ligne.isalpha() or any(x in ligne for x in ["SOMMETS", "ARCS"]):
                    continue
                
                # Vérifier si la ligne est un arc (2 nombres séparés par un espace)
                try:
                    source, cible = map(int, ligne.split())
                    
                    # Ajouter les arcs au graphe
                    if source not in graphe:
                        graphe[source] = []
                    graphe[source].append(cible)
                    
                    # Ajouter les sommets isolés
                    if cible not in graphe:
                        graphe[cible] = []
                except ValueError:
                    # Ligne non conforme à un arc, ignorer silencieusement
                    pass
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
        return {}
    return graphe



def plus_grands_influenceurs(liste_adjacence):
    """
    Identifie les plus grands influenceurs d'un réseau social.
    
    :param liste_adjacence: Dictionnaire représentant le graphe orienté sous forme de liste d'adjacence.
    :return: Liste des sommets qui sont les plus grands influenceurs.
    """
    # Initialisation d'un dictionnaire pour compter les suivis entrants
    suivis_entrants = {sommet: 0 for sommet in liste_adjacence}

    # Parcourir tous les sommets et leurs voisins
    for sommet, voisins in liste_adjacence.items():
        for voisin in voisins:
            suivis_entrants[voisin] += 1  # Un sommet reçoit un suivi entrant

    # Trouver le nombre maximal de suivis entrants
    max_suivi = max(suivis_entrants.values())

    # Identifier tous les sommets qui ont ce nombre de suivis entrants
    influenceurs = [sommet for sommet, suivi in suivis_entrants.items() if suivi == max_suivi]

    return influenceurs
