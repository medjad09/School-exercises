# Demander à l'utilisateur le nombre de photocopies effectuées
nombre_de_photocopies = int(input("Entrez le nombre de photocopies effectuées : "))

# Initialiser la facture à zéro
facture = 0.0

# Calculer la facture en fonction du nombre de photocopies
if nombre_de_photocopies <= 10:
    facture = nombre_de_photocopies * 0.30
elif nombre_de_photocopies <= 30:
    facture = 10 * 0.30 + (nombre_de_photocopies - 10) * 0.25
else:
    facture = 10 * 0.30 + 20 * 0.25 + (nombre_de_photocopies - 30) * 0.20

# Afficher la facture correspondante
print("La facture correspondante est de", facture, "DH")
