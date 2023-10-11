# Demander à l'utilisateur l'âge de l'enfant
age = int(input("Entrez l'âge de l'enfant : "))

# Déterminer la catégorie en fonction de l'âge
if age >= 6 and age <= 7:
    categorie = "Poussin"
elif age >= 8 and age <= 9:
    categorie = "Pupille"
elif age >= 10 and age <= 11:
    categorie = "Minime"
else:
    categorie = "Cadet"

# Afficher la catégorie correspondante
print("Catégorie :", categorie)
