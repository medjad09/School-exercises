A = int(input("Enter number A : "))
B = int(input("Enter number B : "))

if A<0 and B<0 or A>=0 and B>=0:
    C = A
    A = B
    B = C
    print("A =",A)
    print("B =",B)
else:
    print("A + B =",A+B)
    print("A * B =",A*B)
