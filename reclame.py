from algemene_functies import mijn_functie_2
from helper import decoreer

#vraag 5
'''
smaak=input("Welke smaak is in de aanbieding?: ")

while True:
    try:
        prijs=float(input("Wat is de gewone prijs?: "))
        break
    except ValueError:
        print("Oeps! Voer wel een getal in en let erop dat u een punt gebruikt in plaats van een komma.")
        continue

while True:
    try:
        korting=float(input("Hoeveel procent korting? (bijv. 10% korting=0.1): "))
        break
    except ValueError: 
        print("Oeps! Voer wel een heel getal in en let er op dat u een punt gebruikt in plaats van een komma.")
        continue
'''
smaak="aardbei"
prijs=4
korting=0.1

def aanbieding_1(smaak,prijs,korting):
    reclame_prijs=prijs-(prijs*korting)
    # getal afronden naar 2 decimalen: maar 3.60 wordt weergegeven als 3.6 en dat is niet mooi
    reclame_prijs2=round(reclame_prijs,2)
    # {prijs:.2f} voor de opmaak: geeft standaard 2 decimalen weer
    reclametekst= f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} voor {reclame_prijs2:.2f} euro\n"
    return reclametekst
decoreer("Aanbieding/n")
print(aanbieding_1(smaak,prijs,korting))

#vraag 6 en 7
'''
weekinkomen=[]
weekinkomen.append(float(input("Wat was het inkomen op maandag?: ")))
weekinkomen.append(float(input("Wat was het inkomen op dinsdag?: ")))
weekinkomen.append(float(input("Wat was het inkomen op woensdag?: ")))
weekinkomen.append(float(input("Wat was het inkomen op donderdag? ")))
weekinkomen.append(float(input("Wat was het inkomen op vrijdag? ")))
weekinkomen.append(float(input("Wat was het inkomen op zaterdag? ")))
weekinkomen.append(float(input("Wat was het inkomen op zondag? ")))
'''
inkomsten=[220,430,125,160,205,90,345]
btw=0.09
def inkomsten_totaal(inkomsten,btw):
    totaal=0
    for daginkomen in inkomsten:
        totaal += daginkomen
    btw_bedrag=totaal*btw
    totaal_inkomen=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return totaal_inkomen
print(inkomsten_totaal(inkomsten,btw))

#--> optie 2
btw=0.09
def inkomsten_totaal(inkomsten,btw):
    totaal=sum(inkomsten,0)
    btw_bedrag=totaal*btw
    totaal_inkomen=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return totaal_inkomen
print(inkomsten_totaal(inkomsten,btw))


#vraag 8
mijn_lijst=inkomsten
def laag_en_hoog(mijn_lijst):
    laag=min(mijn_lijst)
    hoog=max(mijn_lijst)
    return laag, hoog
print("Het laagste en het hoogste daginkomen: ", laag_en_hoog(mijn_lijst))

#vraag 9 en vraag 10
def gemiddelde(mijn_lijst):
    totaal=0
    for daginkomen in inkomsten:
        totaal += daginkomen
    gemiddeld_inkomen=totaal/(len(mijn_lijst))
    return f"Het gemiddelde daginkomen was {gemiddeld_inkomen} euro."
print(gemiddelde(mijn_lijst))

#-->optie 2
def gemiddelde(mijn_lijst):
    totaal=sum(mijn_lijst)
    gemiddeld_inkomen=totaal/(len(mijn_lijst))
    return f"Het gemiddelde daginkomen was {gemiddeld_inkomen} euro."
print(gemiddelde(mijn_lijst))

#vraag 11
invoer_lijst=[10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
print("Het laagste en het hoogste getal: ", meervoudig(invoer_lijst))

#vraag 12
invoer_lijst_2=3,4
def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    resultaat=mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return resultaat
print(combinatie(invoer_lijst_2))

    
    