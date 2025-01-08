from outils import * 
import random
import sys



def generer_graphe(
    oriente=False, 
    nb_sommets=10, 
    degre_min=1, 
    degre_max=3, 
    nb_communautes=1, 
    prenoms=None, 
    fichier_sortie="graphe.txt"
):
    """
    Génère un graphe aléatoire en respectant les contraintes données.
    Enregistre la représentation textuelle dans un fichier.
    
    Arguments :
        oriente (bool): Si le graphe est orienté ou non.
        nb_sommets (int): Nombre de sommets dans le graphe.
        degre_min (int): Degré minimum des sommets.
        degre_max (int): Degré maximum des sommets.
        nb_communautes (int): Nombre de communautés dans le graphe.
        prenoms (list): Liste de prénoms à utiliser pour les sommets.
        fichier_sortie (str): Nom du fichier de sortie.
    """
    if prenoms is None:
        raise ValueError("Une liste de prénoms doit être fournie pour nommer les sommets.")

    if nb_sommets > len(prenoms):
        raise ValueError("Le nombre de sommets dépasse le nombre de prénoms disponibles.")
    
    # Sélectionner un sous-ensemble de prénoms pour les sommets
    sommets = random.sample(prenoms, nb_sommets)
    graphe = {sommet: [] for sommet in sommets}
    
    # Diviser les sommets en communautés
    communautes = [sommets[i::nb_communautes] for i in range(nb_communautes)]
    for communaute in communautes:
        for sommet in communaute:
            nb_voisins = random.randint(degre_min, min(degre_max, len(communaute) - 1))
            voisins = random.sample([s for s in communaute if s != sommet], nb_voisins)
            graphe[sommet].extend(voisins)

            # Ajouter les arcs/arêtes dans l'autre sens si non orienté
            if not oriente:
                for voisin in voisins:
                    graphe[voisin].append(sommet)

    # Éviter les doublons et créer la liste des arcs/arêtes
    aretes = set()
    for sommet, voisins in graphe.items():
        for voisin in voisins:
            if oriente:
                aretes.add((sommet, voisin))
            else:
                aretes.add(tuple(sorted((sommet, voisin))))

    # Écriture dans le fichier
    with open(fichier_sortie, "w") as f:
        f.write("GRAPHE ORIENTE\n" if oriente else "GRAPHE NON ORIENTE\n")
        f.write(f"{nb_sommets} SOMMETS\n")
        for sommet in sommets:
            f.write(f"{sommet}\n")
        f.write(f"{len(aretes)} {'ARCS' if oriente else 'ARETES'}\n")
        for arete in aretes:
            f.write(" ".join(arete) + "\n")

    print(f"Graphe généré et enregistré dans le fichier {fichier_sortie}.")



def temps_propagation(liste_adjacence, source, cible):
    """
    Calcule le temps minimum de propagation d'une information entre une source et une cible.

    :param liste_adjacence: Dictionnaire représentant le graphe sous forme de liste d'adjacence.
                            Les clés sont les personnes et les valeurs sont des listes de personnes suivies.
    :param source: Personne source de l'information.
    :param cible: Personne cible de l'information.
    :return: Temps minimum de propagation (en minutes) ou None si la cible n'est pas atteignable.
    """
    # Exécuter le parcours en largeur pour obtenir les distances depuis la source
    distances = parcours_largeur(liste_adjacence, source)
    
    # Vérifier si la cible est atteignable
    if cible not in distances:
        return None 
    
    # Récupérer la distance minimale en termes de nombre d'arêtes
    distance_arcs = distances[cible]
    
    # Calculer le temps total de propagation (5 minutes par lien)
    temps_total = distance_arcs * 5
    return temps_total

def chemin_propagation(graphe, source, cible):
    """
    Retourne le chemin minimum entre une source et une cible dans un graphe orienté.

    :param graphe: dict, le graphe représentant les relations entre les personnes
    :param source: str, la personne source de l'information
    :param cible: str, la personne cible de l'information
    :return: list, une liste représentant le chemin minimum ou None si aucun chemin n'existe
    """
    # Utilise parcours_largeur pour trouver le chemin minimum
    chemin = parcours_largeur(graphe, source, cible)
    
    # Retourner le chemin ou None si aucun chemin n'existe
    if chemin is None:
        return None
    return chemin


