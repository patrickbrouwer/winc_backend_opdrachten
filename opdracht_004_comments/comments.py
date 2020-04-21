
# 1. maak 3 variabelen, elke variabele naam is de naam van een product uit de supermarkt, elk product heeft een prijs in hele euro's. Voorbeeld: `broccoli = 2`
melk = 2
roomijs = 3
pampers = 9

# 2. tel de producten bij elkaar op, stop de nieuwe waarde in een variabele
subtotal = (melk + roomijs + pampers)

# 3. bereken de gemiddelde prijs van de producten
avgprice = (subtotal/3)

#     1. rond dit getal af tot 2 cijfers achter de komma
round(avgprice, 2)

#     2. stop het resultaat in een variabele
avgpriceround = round(avgprice, 2)

# 4. maak voor elk product een "aantal" variabele aan: `aantalBroccoli = 5`
amountMelk = 6
amountRoomijs = 3
amountPampers = 2  # 2 pakken pampers op voorraad

# 5. bereken de totaalprijs en stop die in een variabele
totalPrice = (amountMelk*melk + amountRoomijs*roomijs + amountPampers*pampers)

# 6. maak een variabele `kortingPercentage` (dus tussen 0 en 100)
discountPercentage = 26  # korting van 26%

# 7. bereken de totaalprijs, met korting, tot 2 cijfers achter de komma. Denk goed na over de volgorde van korting eraf halen en afronden.
total = round((totalPrice/100) * (100-discountPercentage), 2)
print(total)

"""
Gemaakt voor de Python course van Winc Academy

Copyright (dacht het niet!)
"""
