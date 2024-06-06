############################ FONCTIONNEMENT ###################################

Deux script /launch.sh permettent de lancer la solution de manière séparée
entre le problème du drone ainsi que des vehicules.
Cela executera un script en python3 qui affichera dans le terminal les distances
calculer et qui mettra les chemins à utiliser dans un fichier
path.txt sous forme de (noeud_source, noeud_destination).

############################ ARBORESCENCE #####################################

./
|
|- AUTHORS -> les auteurs du projet
|- README -> ce fichier
|- 1_drone/
|     |-- launch.sh -> le script de lancement
|     |-- graph.xml -> le graph stocké sous format xml
|     |-- main.py   -> la solution en python3
|     |-- path.txt  -> le chemin retenu par l'algorithme
|
|- 2_deneigeuse/
      |-- launch.sh -> le script de lancement
      |-- graph.xml -> le graph stocké sous format xml
      |-- main.py   -> la solution en python3
      |-- path.txt  -> le chemin retenu par l'algorithme
      |-- out/
            |-- les sous graphes en fonction du nombre de déneigeuse

################################ PREREQUIS ##########################################

Necesite python3, python3-pip et python3.10-venv installer.

################################ NOTE ##########################################

Les solutions pythons ne fonctionne pas sur le NixOS.
(pandas necesite libstdc++.so.6 qui n'est pas accessible)