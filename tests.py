from outils import (
    nouvelle_file,
    enfiler,
    defiler,
    file_vide,
    nouvelle_pile,
    empiler,
    depiler,
    pile_vide,
    parcours_profondeur
)
from outils import nombre_aretes_matrice, nombre_aretes_liste, nombre_d_arcs_matrice, nombre_d_arcs_liste, charger_graphe,parcours_largeur, generer_graphe, generer_liste, generer_matrice

import graphe

def test_file():
    
    file = nouvelle_file()
    assert file_vide(file) == True  

    # Test de l'enfilement
    enfiler(file, 1)
    enfiler(file, 2)
    enfiler(file, 3)
    assert file_vide(file) == False  

    # Test du défilement
    assert defiler(file) == 1 
    assert defiler(file) == 2  
    assert defiler(file) == 3  
    assert file_vide(file) == True  


def test_pile():

    pile = nouvelle_pile()
    assert pile_vide(pile) == True 

    # Test de l'empilement
    empiler(pile, 1)
    empiler(pile, 2)
    empiler(pile, 3)
    assert pile_vide(pile) == False   

    # Test du dépilement
    assert depiler(pile) == 3  
    assert depiler(pile) == 2  
    assert depiler(pile) == 1  
    assert pile_vide(pile) == True  

test_file()
print("Tous les tests pour les files ont réussi.")

test_pile()
print("Tous les tests pour les piles ont réussi.")

def test_nombre_aretes_matrice(matrice_adj):

    resultat = nombre_aretes_matrice(matrice_adj)
    pile = []

    # On ajoute des éléments dans la pile pour chaque arête
    for _ in range(resultat): 
        empiler(pile, 1)

    # Vérifie que le nombre d'arêtes correspond en dépilant les éléments
    while not pile_vide(pile):  
        depiler(pile)

    assert pile_vide(pile)

test_nombre_aretes_matrice(graphe.Mat)
print("Test pour la matrice d'adjacence réussi.")


def test_nombre_aretes_liste(liste_adj):
   
    resultat = nombre_aretes_liste(liste_adj)
    pile = []

    # On ajoute des éléments dans la pile pour chaque arête
    for _ in range(resultat):  
        empiler(pile, 1)

    # Vérifie que le nombre d'arêtes correspond en dépilant les éléments
    while not pile_vide(pile):  
        depiler(pile)

    assert pile_vide(pile)

test_nombre_aretes_liste(graphe.Adj)
print("Test pour la liste d'adjacence réussi.")

def test_nombre_d_arcs_matrice(matrice_adjacence):
    
    resultat = nombre_d_arcs_matrice(matrice_adjacence)
    
    pile = []
    for _ in range(resultat):
        empiler(pile, 1)
    
    while not pile_vide(pile):
        depiler(pile)

    assert pile_vide(pile)  # Vérifie que la pile est vide


test_nombre_d_arcs_matrice(graphe.Mat)
print("Test pour la fonction nombre_d_arcs_matrice réussi.")

def test_nombre_d_arcs_liste(liste_adjacence):

    resultat = nombre_d_arcs_liste(liste_adjacence)
    
    pile = []
    for _ in range(resultat):
        empiler(pile, 1)
    
    while not pile_vide(pile):
        depiler(pile)

    assert pile_vide(pile)  # Vérifie que la pile est vide

# Appel du test
test_nombre_d_arcs_liste(graphe.Adj)
print("Test pour la fonction nombre_d_arcs_liste réussi.")

def test_charger_graphe(fichier_test):
    """
    Teste la fonction charger_graphe avec un fichier donné.

    :param fichier_test: Chemin du fichier de description du graphe.
    """
    print(f"Test du fichier : {fichier_test}")

    # Test de la représentation en matrice
    sommets, matrice = charger_graphe(fichier_test, representation='matrice')
    print("Représentation en matrice d'adjacence :")
    print("Sommets :", sommets)
    print("Matrice :", matrice)

    # Validation basique pour la matrice d'adjacence
    assert len(sommets) == len(matrice), "Le nombre de sommets et la taille de la matrice ne correspondent pas."

    for i in range(len(matrice)):
        assert len(matrice[i]) == len(matrice), "La matrice doit être carrée."

    # Test de la représentation en liste d'adjacence
    sommets, liste_adj = charger_graphe(fichier_test, representation='liste')
    print("Représentation en liste d'adjacence :")
    print("Sommets :", sommets)
    print("Liste d'adjacence :", liste_adj)

    # Validation basique pour la liste d'adjacence
    assert len(sommets) == len(liste_adj), "Le nombre de sommets et la taille de la liste d'adjacence ne correspondent pas."

    for sommet in liste_adj:
        assert sommet in sommets, f"Le sommet {sommet} dans la liste d'adjacence n'existe pas dans la liste des sommets."

    print("Tous les tests sont passés avec succès.")

# Demande le fichier de test directement lorsque le script est exécuté
fichier_test = input("Entrez le chemin du fichier de graphe : ")
try:
    test_charger_graphe(fichier_test)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{fichier_test}' n'existe pas.")
except Exception as e:
    print(f"Erreur lors de l'exécution du test : {e}")

def test_parcours_largeur(matrice, sommet_depart):
    """
    Teste la fonction de parcours en largeur avec une matrice donnée et un sommet de départ.

    :param matrice: La matrice d'adjacence à utiliser pour le test.
    :param sommet_depart: Le sommet de départ pour le parcours en largeur.
    """

    resultat = parcours_largeur(matrice, sommet_depart)
    
    # Créer une file pour simuler les sommets explorés
    file = nouvelle_file()
    for sommet in resultat:
        enfiler(file, sommet)
    
    # Vérification que la file est vide après avoir dépilé tous les éléments
    while not file_vide(file):
        defiler(file)

    # La file doit être vide si tout a été correctement traité
    assert file_vide(file)
    print(f"Test réussi pour le sommet de départ {sommet_depart} avec la matrice donnée.")



def test_parcours_profondeur(matrice, sommet_depart):

    resultat = parcours_profondeur(matrice, sommet_depart)
    
    # Vérifie que tous les sommets atteignables depuis le sommet de départ sont explorés
    pile = nouvelle_pile()
    for sommet in resultat:
        empiler(pile, sommet)
    
    while not pile_vide(pile):
        depiler(pile)

    assert pile_vide(pile), f"Erreur dans le parcours en profondeur depuis le sommet {sommet_depart}"
    print(f"Test réussi pour le sommet de départ {sommet_depart} avec la matrice donnée.")