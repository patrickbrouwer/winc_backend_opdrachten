# 1. maak een variabele aan voor elke speler
# 2. voorbeeld: `hans = 'Hans van Breukelen'`
hans = 'Hans van Breukelen'
print(hans)
berry = 'Berry van Aerle'
print(berry)
frank = 'Frank Rijkaard'
print(frank)
ronald = 'Ronald Koeman'
print(ronald)
adri = 'Adri van Tiggelen'
print(adri)
gerald = 'Gerald Vanenburg'
print(gerald)
arnold = 'Arnold Mühren'
print(arnold)
jan = 'Jan Wouters'
print(jan)
erwin = 'Erwin Koeman'
print(erwin)
marco = 'Marco van Basten'
print(marco)
ruud = 'Ruud Gullit'
print(ruud)
joop = 'Joop Hiele'
print(joop)
wilbert = 'Wilbert Suvrijn'
print(wilbert)
john = 'John van \'t Schip'
print(john)
john2 = 'John Bosman'
print(john2)
wim = 'Wim Kieft'
print(wim)

# 3. maak een variabele aan voor de minuten waarin gescoord is
goalTime1 = 35
goalTime2 = 54
print(goalTime1)
print(goalTime2)

# 4. maak met de `+` een nieuwe string van alle spelers die gescoord hebben, er moet een komma tussen
print('Tijdens deze wedstrijd hebben de volgende spelers gescoord: ' +
      ruud + (',') + marco)

# 5. gebruik string interpolatie met de namen en minuten om een string zoals de volgende te maken.
#    Het resultaat moet één string zijn. Dus de nieuwe regel erin moet een onderdeel zijn van die ene string.
print((ruud + ' scoorde in de 35e minuut.') +
      '\n' + (ronald + ' scoorde in de 54e minuut'))


# Deel 2
# 1. gebruik een combinatie van slicen en `find` om van een speler de voornaam te krijgen
firstName = hans[0:hans.find(' ')]
print(firstName)


# 2. gebruik een combinatie van `find`, slicen en `len` om de lengte van de achternaam van een speler te bepalen
lastName = hans[hans.find(' ')+1:]
print(lastName)

lenghtLastName = len(lastName[hans.find("")+1:])
print("lenght last name:", lenghtLastName)


# 3. geef bij een speler niet de hele voornaam, alleen de eerste letter en een punt, voorbeeld: `H. van Breukelen`
hans_initial = hans[0:1] + ". " + hans[hans.find(" ")+1:]
print(hans_initial)


# 4. herhaal met de `*` de voornaam van een speler, met uitroepteken en spatie, even vaak als de letters in zijn voornaam, voorbeeld: `Hans! Hans! Hans! Hans!` (want Hans is 4 letters). Zorg dat het eindresultaat niet een spatie aan het einde over heeft
hans_4_times = (len(hans[0:hans.find(" ")]) *
                (hans[0:hans.find(" ")]+"! ")).strip(" ")
print(hans_4_times)

# 5. check met `==` of de laatste letter van de vorige opdracht een spatie is (dat geeft True of False terug)
print(hans_4_times[-1] == " ")
