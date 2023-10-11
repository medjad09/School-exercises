# Saisie du nombre de départ
nombre_depart = int(input("Entrez un nombre de départ : "))

# Initialisation d'un compteur
compteur = 1

# Utilisation de la boucle Tant que pour afficher les dix nombres suivants
while compteur <= 10:
    nombre_suivant = nombre_depart + compteur
    print(nombre_suivant)
    compteur += 1
