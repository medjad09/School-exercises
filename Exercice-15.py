# Saisie du nombre positif non nul
n = int(input("Entrez un nombre positif non nul : "))

# Vérification que le nombre est positif et non nul
if n <= 0:
    print("Le nombre doit être positif et non nul.")
else:
    factorielle = 1

    # Calcul de la factorielle
    for i in range(1, n + 1):
        factorielle *= i

    # Affichage du résultat
    print(f"La factorielle de {n} est : {factorielle}")
