# Saisie de l'entier n
n = int(input("Entrez un entier n : "))

U0 = 6
U = U0

for i in range(1, n + 1):
    U = 4 * U + 10

print(f"La valeur de U{n} est : {U}")
