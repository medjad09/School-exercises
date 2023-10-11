# Saisie de deux nombres entiers
nombre1 = int(input("Entrez le premier nombre entier : "))
nombre2 = int(input("Entrez le deuxième nombre entier : "))

# Saisie de l'opérateur avec vérification
while True:
    operateur = input("Entrez l'opérateur (+, -, *, /) : ")
    if operateur in ('+', '-', '*', '/'):
        break
    else:
        print("Opérateur invalide. Veuillez réessayer.")

# Exécution de l'opération
if operateur == "+":
    resultat = nombre1 + nombre2
elif operateur == "-":
    resultat = nombre1 - nombre2
elif operateur == "*":
    resultat = nombre1 * nombre2
else:  # L'opérateur est '/'
    if nombre2 != 0:
        resultat = nombre1 / nombre2
    else:
        print("Division par zéro n'est pas autorisée.")
        resultat = None

# Affichage du résultat
if resultat is not None:
    print("Résultat :", resultat)
