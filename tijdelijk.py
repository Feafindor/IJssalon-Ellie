#vraag 2
prijzen={"aardbei":float(3),"vanille":float(4),"chocolade":float(5)}
#vraag 3
aanbieding=(prijzen["aardbei"]*0.8)
#vraag 4
reclame_tekst=(f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}")
print("\n")
print(reclame_tekst)
print("\n")
#vraag 5
print(reclame_tekst.index("0"))
reclame_tekst2=reclame_tekst[:62]
print(reclame_tekst2)
print("\n")
#vraag 6
reclame_tekst3=reclame_tekst2.upper()
print(reclame_tekst3)
print("\n")
#vraag 7
reclame_tekst4=reclame_tekst3.split(" ")
print(reclame_tekst4)
print("\n")
#vraag 8
print("Zo ziet het eruit als het onder elkaar staat:")
for woord in reclame_tekst4:
    print(woord)
print("\n")
#vraag 9
reclame_tekst5=reclame_tekst3.lower()
print(reclame_tekst5)
print("\n")
#vraag10
for woord in reclame_tekst4:
    if len(woord) > 4:
        print(woord.upper())
    else:
        print(woord.lower())