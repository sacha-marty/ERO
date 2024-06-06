############################ FONCTIONNEMENT ###################################

Deux script /launch.sh permettent de lancer la solution de manière séparée
entre le problème du drone ainsi que des vehicules.
Cela executera un script en python3 qui affichera dans le terminal les distances
calculer et qui mettra les chemins à utiliser dans un fichier
path.txt sous forme de (noeud_source, noeud_destination).

################################ DEMO #########################################

Pour lancer la demo du drone:
* lancer launch.sh en etant dans Drone/

Pour lancer la demo des Vehicules:
* lancer launch.sh ~Quartier~ en etant dans Vehicules/
  avec ~Quartier~ le quartier de Monreal que vous voulez faire.

############################ ARBORESCENCE #####################################

./
|
|- AUTHORS -> les auteurs du projet
|- README -> ce fichier
|- Drone/
|     |-- launch.sh -> le script de lancement
|     |-- graph.xml -> le graph stocké sous format xml (Generer)
|     |-- main.py   -> la solution en python3
|     |-- path.txt  -> le chemin retenu par l'algorithme (Generer)
|     |-- clear.sh  -> le script de netoyage, retire les fichiers generer et le dossier de l'environement python
|
|- Vehicules/
      |-- launch.sh -> le script de lancement
      |-- graph.xml -> le graph stocké sous format xml (Generer)
      |-- main.py   -> la solution en python3
      |-- path.txt  -> le chemin retenu par l'algorithme (Generer)
      |-- clear.sh  -> le script de netoyage, retire les fichiers generer et le dossier de l'environement python
      |-- out/
            |-- les sous graphes en fonction du nombre de déneigeuse

################################ PREREQUIS ##########################################

Necesite python3, python3-pip et python3.10-venv installer.

################################ NOTE ##########################################

Les solutions pythons ne fonctionne pas sur le NixOS.
(pandas necesite libstdc++.so.6 qui n'est pas accessible)
