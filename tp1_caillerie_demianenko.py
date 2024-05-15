import matplotlib.pyplot as plt

## Ouverture du fichier
texte = open(r"/Users/veroniquedemianenko/Desktop/bigdata/tp1/texte_Shakespeare.txt", 'r')
texte = texte.readlines()
texte = [mot.strip() for mot in texte]  # On supprime les '\n' marquant le saut de ligne

# On travaille dans ce TP sur le document texte_Shakespeare

## Choix de la taille de la table de hachage
print('Nombre de lignes:', len(texte))

M = len(texte)*3

# M n'est pas premier donc on prend le nombre premier suivant

# Ici on prend
M = 68729

## Ce dont on a besoin
import string
from math import floor, sqrt

alphabet = list(string.ascii_lowercase)
utf8_alphabet = [ord(letter) for letter in alphabet]


## Fonction de hachage par division
def emilie_veronique_hachagediv(mot,M): # mot est une chaîne de caractère
    mot = list(mot.lower())
    nombre = 0
    for i in range(len(mot)):
        indice = utf8_alphabet[alphabet.index(mot[i])]
        nombre += indice*(26**(len(mot)-i-1)) # association nombre <-> mot comme en cours
    h = nombre%M
    return h

## Fonction de hachage par multiplication
A = ( sqrt(5) - 1 ) / 2

def emilie_veronique_hachagemult(mot,M): # mot est une chaîne de caractère
    mot = list(mot)
    nombre = 0
    for i in range(len(mot)):
        indice = alphabet.index(mot[i])
        nombre += indice*(26**(len(mot)-i-1))
    h = floor( M * (nombre * A - floor(nombre *A) ) )
    return h


## Nombre de collisions
def nbcolldiv(texte,M):
    hachage = [0]*M
    nb_coll = [0]*M
    somme_coll = 0
    for mot in texte:
        indice = emilie_veronique_hachagediv(mot,M)
        if hachage[indice] == 0:
            hachage[indice] = mot
        else:
            nb_coll[indice] += 1
            somme_coll+=1
    return [nb_coll, somme_coll]

def nbcollmult(texte,M):
    hachage = [0]*M
    nb_coll = [0]*M
    somme_coll=0
    for mot in texte:
        indice = emilie_veronique_hachagemult(mot,M)
        if hachage[indice] == 0:
            hachage[indice] = mot
        else:
            nb_coll[indice] += 1
            somme_coll+=1
    return [nb_coll, somme_coll]

print('Nombre de collisions pour le hachage par division :', nbcolldiv(texte,M)[1])
print('Nombre de collisions pour le hachage par multiplication :', nbcollmult(texte,M)[1])

indice=[i for i in range(M)]

## Affichage des collisions pour la fonction de hachage de division

plt.plot(indice, nbcolldiv(texte,M)[0], label='Division')
#plt.plot(range(M), nb_coll_mult, label='Multiplication')
plt.xlabel('Indice dans la table de hachage')
plt.ylabel('Nombre de collisions')
plt.title('Nombre de collisions en fonction de l\'indice dans la table de hachage')
plt.legend()
plt.show()

## Affichage des collisions pour la fonction de hachage de multiplication
plt.plot(indice, nbcollmult(texte,M)[0], label= 'Multiplication')
plt.xlabel('Indice dans la table de hachage')
plt.ylabel('Nombre de collisions')
plt.title('Nombre de collisions en fonction de l\'indice dans la table de hachage')
plt.legend()
plt.show()





