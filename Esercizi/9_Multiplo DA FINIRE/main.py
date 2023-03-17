def trova_divisore(a,b):
    divisore = 0
    while True:
        for i in range(a, b):
            try:
                while divisore % i != 0:
                    divisore += 1
                    if divisore % i == 0:
                        break
            except TypeError:
                print("Valore non valido.")
    return divisore

while True:
    a = int(input("Inserisci il primo numero:"))
    b = int(input("Inserisci il secondo numero:"))
    if b > a:
        break
    print("Il secondo numero deve essere piu' grande del primo")
print(trova_divisore(a,b))