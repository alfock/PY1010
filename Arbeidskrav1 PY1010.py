# -*- coding: utf-8 -*-
"""
Arbeidskrav 1 PY1010-1 26 sammenligning av årlige bilkostnader
Programmet skal beregne årlige kostander for en elbil og bensinbil. 
Til slutt beregnes forskjellen mellom de 2 biltypene
"""


#Kjørelengde

#Brukeren skriver inn hvor mange kilometer bilen køres pr år
km_per_aar = int(input("Hvor mange kilometer kjører du per år?"))

#Forsikring

forsikring_elbil= 5000
forsikring_bensinbil= 7500

#Trafikkforsinkringsavgift

#Avgiften er lik for begge biltypene
trafikkavgift_per_dag= 8.38

#Regner ut avgiften for ett år
trafikkavgift_per_aar= trafikkavgift_per_dag* 365

#Drivstoff og strøm

#Elbilen bruker 0.2 kwh per kilometer
stromforbruk_per_km = 0.2

#Strømprisen er satt til 2 kroner per kwh
strompris= 2.0 

#Besinbilen koster 1 krone per kilometer i drivstoff
bensinpris_per_km = 1.0 

#Regner ut årlige kostnader til drivstoff og strøm
stromkostnad= km_per_aar * stromforbruk_per_km * strompris
bensinkostnad= km_per_aar * bensinpris_per_km

#Bomavgifter

bom_elbil_per_km= 0.1 
bom_bensinbil_per_km= 0.3 

#Regner ut årlige bomkostnader
bom_elbil= km_per_aar* bom_elbil_per_km
bom_bensinbil= km_per_aar *bom_bensinbil_per_km

#Totale årlige kostander

totalkostnad_elbil = (
    forsikring_elbil
    + trafikkavgift_per_aar
    +stromkostnad
    +bom_elbil
    )

totalkostnad_bensinbil= (
    forsikring_bensinbil
    + trafikkavgift_per_aar
    + bensinkostnad
    +bom_bensinbil
    )

#Regner ut hvor mye dyrere bensinbilen er per år
kostnadsforskjell= totalkostnad_bensinbil - totalkostnad_elbil

#Skriver resultater til skjermen

print()
print ("Årlige kostnader")
print("-----------------")

print(f"Elbil: {totalkostnad_elbil:.2f} kr")
print(f"Bensinbil: {totalkostnad_bensinbil:.2f} kr")
print(f"Forskjell: {kostnadsforskjell:.2f} kr")
