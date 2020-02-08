# fibonacci
p1= 0
p2= 1
d = int(input("escriba un numero: "))
d=d-1
i = 0
while i <= d:
    i=i+1
    s = p1 + p2
    p1 = p2
    p2= s
    print(f"la posicion {i} es igual a {s}")