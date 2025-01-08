import argparse
import random

# La fonction generer_graphe à utiliser (identique à celle que tu as fournie plus tôt)
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

# Configuration de l'argument parser
def main():
    parser = argparse.ArgumentParser(description="Générer un graphe aléatoire avec différentes options.")
    
    parser.add_argument('--oriente', action='store_true', help="Générer un graphe orienté")
    parser.add_argument('--nb_sommets', type=int, default=10, help="Nombre de sommets dans le graphe (par défaut 10)")
    parser.add_argument('--degre_min', type=int, default=1, help="Degré minimum des sommets (par défaut 1)")
    parser.add_argument('--degre_max', type=int, default=3, help="Degré maximum des sommets (par défaut 3)")
    parser.add_argument('--nb_communautes', type=int, default=1, help="Nombre de communautés dans le graphe (par défaut 1)")
    parser.add_argument('--prenoms', type=str, help="Liste de prénoms séparés par des virgules à utiliser pour les sommets.")
    parser.add_argument('--fichier_sortie', type=str, default="graphe.txt", help="Nom du fichier de sortie (par défaut 'graphe.txt')")

    args = parser.parse_args()

    # Validation du paramètre prenoms
    if args.prenoms:
        prenoms = args.prenoms.split(",")
    else:
        prenoms = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Franck", "Grace", "Hannah", "Igor", "Jack",
    "Katherine", "Louis", "Marie", "Nina", "Oscar", "Paul", "Quentin", "Rachel", "Samuel", "Tina",
    "Ursula", "Victor", "Wendy", "Xavier", "Yasmine", "Zoe"] 

    # Appel de la fonction de génération du graphe avec les arguments reçus
    generer_graphe(
        oriente=args.oriente,
        nb_sommets=args.nb_sommets,
        degre_min=args.degre_min,
        degre_max=args.degre_max,
        nb_communautes=args.nb_communautes,
        prenoms=prenoms,
        fichier_sortie=args.fichier_sortie
    )

if __name__ == '__main__':
    main()
