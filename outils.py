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


print(nombre_aretes_matrice(graphe.Mat))
print(nombre_aretes_liste(graphe.Adj))

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

print(nombre_d_arcs_matrice(graphe.Mat))
print(nombre_d_arcs_liste(graphe.Adj))
