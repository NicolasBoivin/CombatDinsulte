# Combat d'insultes

Combat d'insultes est un jeu de mots amusant où les joueurs s'affrontent en construisant des phrases offensantes pour insulter leur adversaire. Les joueurs choisissent un personnage avec des faiblesses spécifiques et marquent des points en construisant des phrases qui exploitent ces faiblesses.

## Structure du projet

Le projet est organisé en plusieurs fichiers Python pour une meilleure modularité :

- `Jeu.py` : Contient la logique principale du jeu, y compris la gestion des joueurs, la construction de phrases, le calcul des scores et la détermination du gagnant.
- `liste_chainee.py` : Implémente une structure de données de liste chaînée pour stocker les phrases construites par les joueurs.
- `mots_phrases.py` : Gère les mots et les phrases utilisés dans le jeu, y compris la génération aléatoire de mots pour différentes catégories.
- `noeuds.py` : Implémente une classe Noeud pour être utilisée dans la structure de liste chaînée.
- `personnage.py` : Définit une classe Personnage avec un nom et une liste de faiblesses.

## Exécution du jeu

Pour exécuter le jeu, vous aurez besoin de Python 3.6 ou ultérieur. Naviguez jusqu'au dossier contenant les fichiers du jeu et exécutez la commande suivante :

python Jeu.py


Le jeu vous invitera à entrer le nombre de tours à jouer, ainsi que les noms des joueurs. Les joueurs choisiront ensuite un personnage et commenceront à construire leurs phrases. Les joueurs peuvent accepter ou passer des mots proposés, ajouter des mots personnalisés ou terminer leurs phrases à tout moment. Une fois tous les tours terminés, le jeu déterminera le gagnant en fonction des scores accumulés.

## Licence

Ce projet est distribué sous la licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le redistribuer selon les termes de la licence.
