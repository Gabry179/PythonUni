import math 

def distanza_pitagorica(x1, y1, z1, x2, y2, z2):
    return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2))

def distanza_manhattan(x1, y1, z1, x2, y2, z2):
    return abs(x1-x2) + abs(y1+2), abs(z1-z2)

def distanza_chebyshev(x1, y1, z1, x2, y2, z2):
    return max(abs(x1-x2),abs(y1-y2),abs(z1-z2))

x1 = float(input("Inserisci x1:"))
y1 = float(input("Inserisci y1:"))
z1 = float(input("Inserisci z1:"))

risposta = input("Vuoi inserire anche x2, y2 e z2? (S/n)")
if risposta == "S":
    x2 = float(input("Inserisci x2:"))
    y2 = float(input("Inserisci y2:"))
    z2 = float(input("Inserisci z2:"))

print("Scegli la metrica:")
metrica = input("p - Pitagorica (Default), m - Manhattan, c - Chebyshev")
if metrica == "":
    metrica = "p"
print(metrica)

if metrica == "p":
    print(distanza_pitagorica(x1, y1, z1, x2=0, y2=0, z2=0))
if metrica == "m":
    print(distanza_manhattan(x1, y1, z1, x2=0, y2=0, z2=0))
if metrica == "c":
    print(distanza_chebyshev(x1, y1, z1, x2=0, y2=0, z2=0))