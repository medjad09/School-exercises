# Saisie de l'entier n
n = int(input("Entrez un entier positif non nul : "))

print("Les diviseurs de", n, "sont :")

# Utilisation d'une boucle for pour trouver les diviseurs
for diviseur in range(1, n + 1):
    if n % diviseur == 0:
        print(diviseur)
