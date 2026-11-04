# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 - PY1010
Denne filen innholder løsningen på oppgave 1-6 og her bruker jeg blandt annet
input, beregninger, funkasjoner, dictionary og plotting. 
Jeg bruker også snake_case for at det skal se ryddig ut.
La også inn capitalize funksjon i oppgave 4b etter at jeg la merke til
feil når man skrev inn land med små bokstaver
"""

import numpy as np
import matplotlib.pyplot as plt
import math


#Oppgave 1

alder = int(input("Hvilket år er du født?"))

#Regner ut hvor gammel personen blir i løpet av 2024
alder_2024= 2024 - alder

print("Du blir", alder_2024, "år i løpet av 2024.")

#Oppgave 2

antall_elever = int(input("Skriv inn antall elever:"))

#Hver elev spiser 1/4 pizza.
#math.ceil runder opp slik at vi kjøper nok pizzaer.
antall_pizza = math.ceil(antall_elever /4)

print("Det må handles inn", antall_pizza, "pizzaer til festen.")

#Oppgave 3

v_grad = float(input("Skriv inn gradtallet: "))

#Funksjon som regner om fra grader til radianer
def grader_til_radianer(v_grad):
    v_rad = v_grad * np.pi / 180
    return v_rad

#Kaller funksjonen og lagrer svaret
v_rad = grader_til_radianer(v_grad)

print(v_grad, "grader tilsvarer", v_rad, "radianer")

#Oppgave 4a

#Dictionary med land, hovedstad og antall innbyggere
#i hovedstaden oppgitt i millioner
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

#Oppgave 4b
#Her la jeg inn .capitalize etter at else slo inn ved å skrive landet med
#små bokstaver
land = input("Skriv inn et land:").capitalize()

#Sjekker om landet finnes i dictionaryen 
if land in data: 
    hovedstad = data [land][0]
    innbyggere = data[land][1]
    
    print(
        hovedstad,
        "er hovedstaden i",
        land,
        "og det er",
        innbyggere,
        "mill. innbyggere i",
        hovedstad
        )
else:
        print("Landet finnes ikke i dictionaryen.")
        
# Oppgave 4c

nytt_land = input("Skriv inn et nytt land: ")
ny_hovedstad = input("Skriv inn hovedstaden: ")
nye_innbyggere = float(
    input("Skriv inn antall innbyggere i hovedstaden i millioner: ")
    )
# Legger det nye landet inn i dictionaryen
data[nytt_land] = [ny_hovedstad, nye_innbyggere]

print("Den oppdaterte dictionaryen er:")
print(data)

# Oppgave 5

"""
Figuren består av en rettvinklet trekant og en halvsirkel.

Siden a er både den ene kateten i trekanten og diameteren til halvsirkelen.
"""

def beregn_figur(a, b):
    
    #Radiusen til halvsirkelen
    radius = a/ 2
    
    #Arealet av trekanten
    areal_trekant = a*b / 2 
    
    #Arealet av halvsirkelen
    areal_halvsirkel = np.pi * radius**2 / 2 
    
    # Totalt areal
    areal = areal_trekant + areal_halvsirkel
    
    #Finner hypotenusen med Pytagoras
    hypotenus = np.sqrt(a**2 + b**2)
    
    #Lengden på buen til halvsirkelen
    bue_halvsirkel = np.pi * radius
    
    #Ytre omkrets
    #Siden a tas ikke med fordi den ligger inne i figuren
    omkrets = b + hypotenus + bue_halvsirkel
    
    return areal, omkrets

a= float(input("Sriv inn lengden a: "))
b= float(input("Skriv inn lengden b: "))
# Kaller funksjonen
areal, omkrets = beregn_figur(a, b)

print("Arealet til figuren er:", round(areal, 2))
print("Den ytre omkretsen er:", round(omkrets, 2))

# Oppgave 6

# Lager 200 x-verdier mellom -10 og 10
x = np.linspace(-10, 10, 200)

# Funksjonen f(x) = -x^2 - 5
y = -x**2 - 5

#Plotter funksjonen
plt.plot(x, y)

# Legger til tekst på grafen 
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = -x^2 - 5")

# Viser rutenett og graf
plt.grid()
plt.show()
    