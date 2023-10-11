# Saisie du nombre n
n = int(input("Entrez un entier n : "))

somme = 0
entier_impair = 1

for i in range(n):
    somme += entier_impair ** 2
    entier_impair += 2

print(f"La somme des carrés des {n} premiers entiers impairs est : {somme}")
