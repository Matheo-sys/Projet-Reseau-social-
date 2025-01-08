from outils import * 

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
