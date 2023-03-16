def encrypt(stringa):
    nuovaStr = ""
    for i in stringa:
        if i >= 'a':
            if ord(i)+3 <= 122:
                ascii = chr(ord(i)+3)
                nuovaStr += ascii
            else:
                ascii = chr(ord(i)+3-26)
                nuovaStr += ascii
        else:
            print(f"Il carattere {i} non e' valido.")
    return nuovaStr
    
def decrypt(stringa):
    nuovaStr = ""
    for i in stringa:
        if i >= 'a':
            if ord(i)-3 >= 97:
                ascii = chr(ord(i)-3)
                nuovaStr += ascii
            else:
                ascii = chr(ord(i)-3+26)
                nuovaStr += ascii
        else:
            print(f"Il carattere {i} non e' valido.")
    return nuovaStr