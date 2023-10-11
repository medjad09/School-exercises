# Saisie de l'entier n
n = int(input("Entrez un entier supérieur à 2 : "))

if n <= 2:
    print("Veuillez saisir un entier supérieur à 2.")
else:
    U0, U1 = 0, 1
    Un = U0 + U1
    fibonacci = [U0, U1]

    while Un <= n:
        fibonacci.append(Un)
        U0, U1 = U1, Un
        Un = U0 + U1

    print(f"Suite de Fibonacci jusqu'à {n} :")
    for terme in fibonacci:
        print(terme)
