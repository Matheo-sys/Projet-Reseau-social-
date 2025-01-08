from main import *
from outils import *

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Génération de graphes aléatoires.")
    parser.add_argument("--oriente", action="store_true", help="Créer un graphe orienté.")
    parser.add_argument("--nb_sommets", type=int, default=10, help="Nombre de sommets du graphe.")
    parser.add_argument("--degre_min", type=int, default=1, help="Degré minimum des sommets.")
    parser.add_argument("--degre_max", type=int, default=3, help="Degré maximum des sommets.")
    parser.add_argument("--nb_communautes", type=int, default=1, help="Nombre de communautés.")
    parser.add_argument("--fichier_sortie", type=str, default="graphe.txt", help="Nom du fichier de sortie.")
    
    args = parser.parse_args()

    prenoms = [
        "Adam", "Adrien", "Alexandre", "Antoine", "Arthur", "Benjamin", "Benoît", "Charles", 
        "Christophe", "Daniel", "David", "Dylan", "Édouard", "Éric", "Fabien", "François", 
        "Gabriel", "Geoffrey", "Guillaume", "Hugo", "Jacques", "Jean", "Jérémy", "Jonathan", 
        "Julien", "Kevin", "Léo", "Louis", "Lucas", "Marc", "Mathieu", "Maxime", "Nicolas", 
        "Noah", "Olivier", "Paul", "Pierre", "Quentin", "Raphaël", "Romain", "Samuel", 
        "Simon", "Théo", "Thomas", "Victor", "Vincent", "William", "Xavier", "Yann", "Zacharie",

        "Adèle", "Agnès", "Alice", "Amandine", "Amélie", "Anaïs", "Andréa", "Angélique", 
        "Anne", "Aurélie", "Camille", "Caroline", "Catherine", "Charlotte", "Chloé", 
        "Claire", "Clara", "Coralie", "Éléonore", "Élisabeth", "Élodie", "Émilie", 
        "Emma", "Fanny", "Florence", "Gabrielle", "Hélène", "Inès", "Isabelle", 
        "Jade", "Jeanne", "Julie", "Justine", "Laetitia", "Léa", "Louise", "Lucie", 
        "Manon", "Margaux", "Marie", "Marina", "Mathilde", "Mélanie", "Nathalie", 
        "Noémie", "Océane", "Pauline", "Sarah", "Sophie", "Valentine", "Victoria", "Yasmine", "Zoé",

        "Alex", "Charlie", "Elliot", "Jules", "Milan", "Robin", "Sacha", "Sam", 
        "Toni", "Chris", "Taylor", "Jordan", "Morgan", "Riley", "Jamie", "Cameron"
    ]
    
    generer_graphe(
        oriente=args.oriente,
        nb_sommets=args.nb_sommets,
        degre_min=args.degre_min,
        degre_max=args.degre_max,
        nb_communautes=args.nb_communautes,
        prenoms=prenoms,
        fichier_sortie=args.fichier_sortie
    )
