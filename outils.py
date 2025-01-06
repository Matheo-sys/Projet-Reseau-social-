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

def generer_matrice(sommets, arcs_ou_aretes, orienté):
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

def generer_liste(sommets, arcs_ou_aretes, orienté):
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