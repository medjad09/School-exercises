# Saisie du prix hors taxe et de la catégorie de TVA
prix_ht = float(input("Entrez le prix hors taxe du produit : "))
categorie = input("Entrez la catégorie de TVA (A, B ou C) : ")

# Définir un dictionnaire de taux de TVA pour chaque catégorie
taux_tva = {"A": 0.07, "B": 0.20, "C": 0.25}

# Vérifier si la catégorie est valide
if categorie in taux_tva:
    # Calcul du prix TTC en utilisant le taux de TVA correspondant
    prix_ttc = prix_ht * (1 + taux_tva[categorie])
    print("Le prix TTC du produit est :", prix_ttc)
else:
    print("Catégorie de TVA non valide.")
