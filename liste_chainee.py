from noeud import Noeud

class ListeChainee:
    def __init__(self):
        self.tete = None
        self.queue = None

    def ajouter(self, valeur):
        nouveau_noeud = Noeud(valeur)
        if not self.tete:
            self.tete = nouveau_noeud
            self.queue = nouveau_noeud
        else:
            self.queue.suivant = nouveau_noeud
            self.queue = nouveau_noeud

    def __iter__(self):
        noeud_courant = self.tete
        while noeud_courant:
            yield noeud_courant.valeur
            noeud_courant = noeud_courant.suivant

    def __len__(self):
        return sum(1 for _ in self)

    def __str__(self):
        return ' '.join(str(valeur) for valeur in self)