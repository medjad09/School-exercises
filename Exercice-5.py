n1 = float(input("Bitween the first mark : "))
n2 = float(input("Bitween the second mark : "))
n3 = float(input("Bitween the third mark : "))

while n1<0 or n1>20:
    n1 = float(input("Bitween the first mark : "))
else : 
    while n2<0 or n2>20:
        n2 = float(input("Bitween the second mark : "))
    else : 
        while n3<0 or n3>20: 
            n3 = float(input("Bitween the third mark : "))
m = (n1+n2+n3)/3
if m>=16:
    if int(m)==float(m):
      print(f'The marks average is : ,{int(m)},Very Good.')
    else:
      print(f'The marks average is : ,{round(m,2)},Very Good.')
elif 14<=m<16:
    if int(m)==float(m):
      print(f'The marks average is : ,{int(m)},Good.')
    else:
      print(f'The marks average is : ,{round(m,2)},Good.')
elif 12<=m<14:
    if int(m)==float(m):
      print("The marks average is : ",int(m),"It's ok.")
    else:
      print("The marks average is : ",round(m,2),"It's ok.")
elif 10<=m<12:
    if int(m)==float(m):
      print(f'The marks average is : ,{int(m)},Acceptable.')
    else:
      print(f'The marks average is : ,{round(m,2)},"Acceptable.')
elif m<10:
    if int(m)==float(m):
      print(f'The marks average is : ,{int(m)},Insufficient.')
    else:
      print(f'The marks average is : ,{round(m,2)},"Insufficient.')