import random

class MotsPhrases:
    def __init__(self, sujets, verbes, complements, liaisons, exclamations):
        self.sujets = sujets
        self.verbes = verbes
        self.complements = complements
        self.liaisons = liaisons
        self.exclamations = exclamations

    def generer_mots(self, categorie=None):
        if categorie == "verbes":
            mots = random.choice(self.verbes)
        elif categorie == "complements":
            mots = random.choice(self.complements)
        elif categorie == "liaisons":
            mots = random.choice(self.liaisons)
        elif categorie == "exclamations":
            mots = random.choice(self.exclamations)
        else:
            mots = random.choice(self.sujets)
        return mots