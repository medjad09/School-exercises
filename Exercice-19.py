population_marrakech = 1000000
population_agadir = 500000
annee = 0

while population_agadir <= population_marrakech:
    population_agadir += int(0.08 * population_agadir)  # Augmentation de 8% par an
    population_marrakech += 50000  # Augmentation de 50,000 habitants par an
    annee += 1

print(f"La population de la ville Agadir dépassera celle de Marrakech dans {annee} années.")
