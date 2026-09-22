class Fraction:

    def __init__(self, numérateur, dénominateur):
        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self, n):
        if n % self.dénominateur == 0:
            return True
        else:
            return False

    def valeur(self, n):
        return self.numérateur * (n // self.dénominateur)

class Facteur:

    def __init__(self, facteurs):
        self.facteurs = facteurs

    def nombre(self, L):
        produit = 1
        for i in range(len(L)):
            produit = produit * (self.facteurs[i] ** L[i])

        return produit

    def décomposition(self, n):
        L = []
        for diviseur in self.facteurs:
            n_copie = n
            compteur = 0
            while n_copie % diviseur == 0:
                n_copie = n_copie // diviseur
                compteur += 1
            L.append(compteur)
        return L

class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

    def suite(self, n: int, N: int):
        L = [n]

        while len(L) < N:
            for fraction in self.programme:
                if fraction.est_entier(n):
                    n = fraction.valeur(n)
                    L.append(n)
                    break
            else:
                break

        return L