# Saisie de la valeur de n
n = int(input("Entrez la valeur de n : "))

# Initialisation de la somme
somme = 0.0

# Utilisation d'une boucle for pour calculer la somme
for i in range(1, n + 1):
    somme += 1 / i

# Affichage de la somme
print("La somme est :", somme)
