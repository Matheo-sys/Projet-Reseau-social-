from outils import charger_graphe, plus_grands_influenceurs, parcours_largeur, reseau_une_seule_communaute
import sys

def run_demo(filename):
    print(f"--- Analyse du graphe : {filename} ---")
    
    # 1. Charger le graphe
    try:
        sommets, liste_adj = charger_graphe(filename, representation='liste')
        print(f"Graphe chargé avec {len(sommets)} sommets.")
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return

    # 2. Top influenceurs
    influenceurs = plus_grands_influenceurs(liste_adj)
    print(f"Plus grands influenceurs : {', '.join(map(str, influenceurs))}")

    # 3. Vérification de la connectivité (une seule communauté)
    # On convertit en matrice pour la fonction existante si nécessaire, 
    # mais reseau_une_seule_communaute utilise parcours_largeur qui prend une matrice.
    # On va utiliser la version matrice pour le test de connectivité.
    _, matrice = charger_graphe(filename, representation='matrice')
    est_connecte = reseau_une_seule_communaute(matrice)
    print(f"Le réseau est-il d'une seule communauté ? {'Oui' if est_connecte else 'Non'}")

    # 4. Exemple de parcours de propagation depuis le premier influenceur
    if influenceurs:
        depart = influenceurs[0]
        idx_depart = sommets.index(depart)
        visites = parcours_largeur(matrice, idx_depart)
        print(f"Nombre de personnes pouvant être atteintes par {depart} : {len(visites)}")

    # 5. Test de propagation (Image de 0 vers 1)
    if len(sommets) >= 2:
        s0, s1 = sommets[0], sommets[1]
        chemin = parcours_largeur(liste_adj, s0, cible=s1)
        print(f"Test Propagation (Image de {s0} vers {s1}) :")
        if chemin:
            print(f"  Chemin trouvé : {' -> '.join(chemin)}")
            print(f"  Temps estimé : {(len(chemin)-1)*5} minutes")
        else:
            print(f"  Aucun chemin direct trouvé entre {s0} et {s1}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_demo(sys.argv[1])
    else:
        run_demo("demo_graphe.txt")
