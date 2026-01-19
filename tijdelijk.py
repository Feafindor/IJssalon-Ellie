#vraag 2
prijzen={"aardbei":3,"vanille":4,"chocolade":5}
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
for el in reclame_tekst4:
    print(el)
print("\n")
#vraag 9
print("Toch maar liever in kleine letters...")
for el in reclame_tekst4:
    print(el.lower())
print("\n")
#vraag10
print("Woorden met meer dan 4 letters staan in hoofdletter")
for el in reclame_tekst4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())