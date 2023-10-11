# Saisie de l'âge d'Amal au nième anniversaire
n = int(input("Entrez le nombre d'anniversaires (n) : "))

somme = 0
age = 0

while age < n:
    somme += 500 + 3 * age
    age += 1

print(f"La somme d'argent sur le compte d'Amal lors de son {n}ème anniversaire est de {somme} DH.")
