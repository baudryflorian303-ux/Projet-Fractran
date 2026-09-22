from fractran import Fraction, Facteur, Fractran

somme = [Fraction(3, 2)]
facteurs = Facteur([2, 3, 5])
somme_i_j = []

for i in range(1,11):
    for j in range(1, 11):
        somme_i_j.append(Fractran(somme).run(facteurs.nombre([i, j])))


# Construction de la suite de Fibonacci :

print("Fibonacci rend les couples (F(n), F(n+1)) :")

fibonacci = [Fraction(23, 95), Fraction(57, 23), Fraction(17, 39), Fraction(130, 17), Fraction(11, 14), 
          Fraction(35, 11), Fraction(19, 13), Fraction(1, 19), Fraction(35, 2), Fraction(13, 7), Fraction(7, 1)]

sortie_brute = Fractran(fibonacci).suite(3, 1000) 
sortie = []

for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
        sortie.append(Facteur([2, 3]).décomposition(n))

print(sortie)


# Construction de la suite des nombres premiers :

conway_primegame = [Fraction(17, 91), Fraction(78, 85), Fraction(19, 51), Fraction(23, 38), Fraction(1, 17), 
                    Fraction(11, 13), Fraction(13, 11), Fraction(15, 14), Fraction(15, 2), Fraction(55, 1)]

sortie_brute = Fractran(conway_primegame).suite(2, 100000)
premiers = []

for n in sortie_brute:
    if n == Facteur([2]).nombre(Facteur([2]).décomposition(n)) and n != 2:
        premiers.append(Facteur([2]).décomposition(n)[0])

print(premiers)