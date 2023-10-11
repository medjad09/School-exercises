import math

# Saisie des coefficients de l'équation
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Calcul du discriminant
discriminant = b**2 - 4*a*c

# Vérification du discriminant et calcul des solutions
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Deux solutions réelles distinctes :")
    print("x1 =", x1)
    print("x2 =", x2)
elif discriminant == 0:
    x1 = -b / (2*a)
    print("Une solution réelle :")
    print("x1 =", x1)
else:
    print("Pas de solution réelle")
