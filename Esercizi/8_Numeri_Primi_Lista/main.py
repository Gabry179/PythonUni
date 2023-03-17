def find_primal(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            return num

def primal(a,b):
    for i in range(a, b+1):
        try:
            if(find_primal(i) != None):
                print(find_primal(i))
        except TypeError:
            print("Valore non valido.")

while True:
    a = int(input("Inserisci il primo numero:"))
    b = int(input("Inserisci il secondo numero:"))
    if b > a:
        break
    print("Il secondo numero deve essere piu' grande del primo")
primal(a,b)