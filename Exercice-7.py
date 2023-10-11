# Saisie de l'âge et du sexe de l'habitant
age = int(input("Entrez l'âge de l'habitant : "))
sexe = input("Entrez le sexe de l'habitant (homme ou femme) : ")

# Vérification de l'imposition en fonction de l'âge et du sexe
if sexe == "homme" and age > 20:
    print("Paient l'impot.")
elif sexe == "femme" and 18 <= age <= 35:
    print("Paient l'impot.")
else:
    print("Ne paient pas d'impot.")
