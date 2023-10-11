# Saisie du numéro de mois
mois = int(input("Entrez le numéro du mois (1 pour janvier, 2 pour février, etc.) : "))

# Initialisation du nombre de jours à 0
nombre_de_jours = 0

# Vérification du mois et détermination du nombre de jours
if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
    nombre_de_jours = 31
elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
    nombre_de_jours = 30
elif mois == 2:
    nombre_de_jours = 28  # En supposant une année non bissextile
else:
    print("Mois invalide. Veuillez entrer un numéro de mois valide.")

# Affichage du nombre de jours dans le mois si le mois est valide
if nombre_de_jours > 0:
    print(f"Le mois {mois} a {nombre_de_jours} jours.")
