#!/bin/bash

# Couleurs pour le terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m' # No Color

clear
echo -e "${CYAN}${BOLD}======================================================"
echo -e "         DEMO PROJET RÉSEAU SOCIAL (Matheo-sys)       "
echo -e "======================================================${NC}"

echo -e "\n${YELLOW}${BOLD}[1] ÉTAT D'AVANCEMENT DU PROJET${NC}"
echo -e "${BLUE}Lecture du fichier README.md...${NC}"
cat README.md | sed 's/^/  /'

echo -e "\n${YELLOW}${BOLD}[2] GÉNÉRATION D'UN RÉSEAU SOCIAL${NC}"
echo -e "${BLUE}Commande: python3 script.py --nb_sommets 15 --degre_min 2 --degre_max 5 --nb_communautes 1 --fichier_sortie demo_reseau.txt${NC}"
python3 script.py --nb_sommets 15 --degre_min 2 --degre_max 5 --nb_communautes 1 --fichier_sortie demo_reseau.txt

echo -e "\n${YELLOW}${BOLD}[3] APERÇU DU RÉSEAU GÉNÉRÉ (demo_reseau.txt)${NC}"
echo -e "${BLUE}Affichage des 10 premières lignes :${NC}"
head -n 12 demo_reseau.txt | sed 's/^/  /'

echo -e "\n${YELLOW}${BOLD}[4] ANALYSE DES DONNÉES DU RÉSEAU${NC}"
echo -e "${BLUE}Exécution de demo_features.py...${NC}"
python3 demo_features.py demo_reseau.txt | sed 's/^/  /'

echo -e "\n${YELLOW}${BOLD}[5] EXÉCUTION DES TESTS UNITAIRES${NC}"
echo -e "${BLUE}Vérification de la santé du code (via tests.py)...${NC}"
python3 -c "from tests import run_all_tests; run_all_tests()" | sed 's/^/  /'

echo -e "\n${CYAN}${BOLD}======================================================"
echo -e "            DÉMO TERMINÉE AVEC SUCCÈS !               "
echo -e "======================================================${NC}"
