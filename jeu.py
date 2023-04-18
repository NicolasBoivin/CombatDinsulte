from liste_chainee import ListeChainee
from personnage import Personnage
from mots_phrases import MotsPhrases

class Jeu:
    def __init__(self, personnages, mots_phrases, nombre_tours=5):
        self.personnages = personnages
        self.mots_phrases = mots_phrases
        self.joueurs = []
        self.nombre_tours = nombre_tours


    def choisir_personnage(self):
        for i, personnage in enumerate(self.personnages):
            print(f"{i + 1}. {personnage.nom}")
        choix = int(input("Choisissez un personnage (1 ou 2): "))
        return self.personnages[choix - 1]

    def jouer_tour(self, joueur):
        categorie = None
        if not joueur["phrase"].tete:
            categorie = "sujets"
        elif not joueur["phrase"].queue.suivant:
            categorie = "verbes"
        elif not joueur["phrase"].queue.suivant.suivant:
            categorie = "complements"
        elif not joueur["phrase"].queue.suivant.suivant.suivant:
            categorie = "liaisons"
        else:
            categorie = "exclamations"
        
        mot = self.mots_phrases.generer_mots(categorie)
        print(f"\nMot proposé : {mot}")
        choix = input(f"{joueur['nom']}, tapez 'accepter' pour ajouter le mot à votre phrase, 'passer' pour en obtenir un autre, 'ajouter' pour ajouter un mot personnalisé ou 'terminer' pour terminer votre phrase : ")
        return choix, mot

    def verifier_mot(self, phrase, mot):
        if mot in phrase:
            return False
        return True

    def attribuer_score(self, phrase, personnage):
        longueur = len(phrase)
        impact = sum([sum(1 for mot in phrase if mot == faiblesse) for faiblesse in personnage.faiblesses])
        score = longueur + impact * 2
        return score

    def determiner_gagnant(self):
        gagnant = max(self.joueurs, key=lambda joueur: joueur["score"])
        return gagnant["nom"]

    def demarrer(self):
        print("\nBienvenue dans le combat d'insultes!")
        for i in range(2):
            nom_joueur = input(f"Joueur {i + 1}, entrez votre nom: ")
            personnage = self.choisir_personnage()
            self.joueurs.append({"nom": nom_joueur, "personnage": personnage, "score": 0, "phrase": ListeChainee()})

        tour = 0
        while True:
            joueur = self.joueurs[tour % 2]
            choix, mot = self.jouer_tour(joueur)
            if choix == "terminer":
                joueur["score"] = self.attribuer_score(joueur["phrase"], joueur["personnage"])
                print(f"\n{joueur['nom']}'s phrase : {' '.join(joueur['phrase'])}")
                print(f"Score : {joueur['score']}")
                
                if tour >= self.nombre_tours * 2 - 1:
                    break
            elif choix == "accepter":
                joueur["phrase"].ajouter(mot)
            elif choix == "ajouter":
                mot_personnalise = input("Entrez le mot personnalisé que vous souhaitez ajouter : ")
                joueur["phrase"].ajouter(mot_personnalise)
            else:
                print("Vous avez passé ce mot.")
            
            tour += 1

        gagnant = self.determiner_gagnant()
        print(f"\nLe gagnant est {gagnant}! Félicitations!")

def main():
    personnages = [
        Personnage("Capitaine Crochet", ["crocodile", "Peter Pan"]),
        Personnage("Dracula", ["ail", "soleil"])
    ]

    mots_phrases = MotsPhrases(
        sujets=["Le crocodile", "Peter Pan", "Le soleil", "L'ail"],
        verbes=["mord", "brille", "sent", "provoque"],
        complements=["la peur", "la douleur", "la confusion", "la panique"],
        liaisons=["et", "mais", "car", "donc"],
        exclamations=["quelle horreur!", "incroyable!", "quel cauchemar!", "quelle surprise!"]
    )

    nombre_tours = int(input("Entrez le nombre de tours que vous voulez jouer (un tour par joueur) : "))
    jeu = Jeu(personnages, mots_phrases, nombre_tours)
    jeu.demarrer()

if __name__ == "__main__":
    main()
