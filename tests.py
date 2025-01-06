from outils import (
    nouvelle_file,
    enfiler,
    defiler,
    file_vide,
    nouvelle_pile,
    empiler,
    depiler,
    pile_vide,
)
from outils import nombre_aretes_matrice, nombre_aretes_liste, nombre_d_arcs_matrice, nombre_d_arcs_liste
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
