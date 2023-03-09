stringa = input("Inserisci una parola: ").lower()

def ruota_parole():
    nuovaStr = ""
    for i in stringa:
        if i >= 'a':
            if i < 'z':
                ascii = chr(ord(i)+1)
                nuovaStr += ascii
            else:
                ascii = chr(ord('a'))
                nuovaStr += ascii
        else:
            print(f"Il carattere {i} non e' valido.")
    return nuovaStr

stringa = ruota_parole()
print(stringa)