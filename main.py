from outils import * 
import random

prenoms = [
    # Prénoms masculins
    "Adam", "Adrien", "Alexandre", "Antoine", "Arthur", "Benjamin", "Benoît", "Charles", 
    "Christophe", "Daniel", "David", "Dylan", "Édouard", "Éric", "Fabien", "François", 
    "Gabriel", "Geoffrey", "Guillaume", "Hugo", "Jacques", "Jean", "Jérémy", "Jonathan", 
    "Julien", "Kevin", "Léo", "Louis", "Lucas", "Marc", "Mathieu", "Maxime", "Nicolas", 
    "Noah", "Olivier", "Paul", "Pierre", "Quentin", "Raphaël", "Romain", "Samuel", 
    "Simon", "Théo", "Thomas", "Victor", "Vincent", "William", "Xavier", "Yann", "Zacharie",

    # Prénoms féminins
    "Adèle", "Agnès", "Alice", "Amandine", "Amélie", "Anaïs", "Andréa", "Angélique", 
    "Anne", "Aurélie", "Camille", "Caroline", "Catherine", "Charlotte", "Chloé", 
    "Claire", "Clara", "Coralie", "Éléonore", "Élisabeth", "Élodie", "Émilie", 
    "Emma", "Fanny", "Florence", "Gabrielle", "Hélène", "Inès", "Isabelle", 
    "Jade", "Jeanne", "Julie", "Justine", "Laetitia", "Léa", "Louise", "Lucie", 
    "Manon", "Margaux", "Marie", "Marina", "Mathilde", "Mélanie", "Nathalie", 
    "Noémie", "Océane", "Pauline", "Sarah", "Sophie", "Valentine", "Victoria", "Yasmine", "Zoé",

    # Prénoms neutres ou internationaux
    "Alex", "Charlie", "Elliot", "Jules", "Milan", "Robin", "Sacha", "Sam", 
    "Toni", "Chris", "Taylor", "Jordan", "Morgan", "Riley", "Jamie", "Cameron"
]

def generer_graphe(
    oriente=False, 
    nb_sommets=10, 
    degre_min=1, 
    degre_max=3, 
    nb_communautes=1, 
    distance_max=None, 
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
        distance_max (int): Distance maximale entre deux sommets (pas implémenté dans cette version).
        prenoms (list): Liste de prénoms à utiliser pour les sommets.
        fichier_sortie (str): Nom du fichier de sortie.
    """

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
