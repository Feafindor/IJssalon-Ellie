import helper
import presentatie
import csv
from datetime import datetime

inkomsten={}

while True:
    try:
        inkomsten['Aardbeien-ijs-totaal']=int(input("\nVoer de opbrengsten van Aardbeien-ijs in: "))
        break
    except ValueError:
        print("Voer een geldig getal in.")
        continue

while True:
    try:
        inkomsten["Vanille -ijs-totaal"]=int(input("Voer de opbrengsten van Vanille-ijs in: "))
        break
    except ValueError:
        print("Voer een geldig getal in.")
        continue

while True:
    try:
        inkomsten["Chocolade-totaal"]=int(input("Voer de opbrengsten van Chocolade-ijs in: "))
        break
    except ValueError:
        print("Voer een geldig getal in.")
        continue

while True:
    try:
        inkomsten["Waterijsjes-totaal"]=int(input("Voer de opbrengsten van Waterijsjes in: "))
        break
    except ValueError:
        print("Voer een geldig getal in.")
        continue

'''
inkomsten={"Aardbeien-ijs-totaal":1000,
           "Vanille-ijs-totaal":2000,
           "Chocolade-ijs-totaal":1500,
           "Waterijsjes-totaal":750}
}
'''

resultaat=helper.som(inkomsten)
weergave=presentatie.presenteer2(inkomsten, resultaat)
print(weergave)

datum = datetime.now().strftime("%Y%m%d")
bestandsnaam = f"{datum}boekhouding.csv"
with open(bestandsnaam,"w",newline='') as csvfile:
    veldnamen=["Product","Opbrengst"]
    schrijver=csv.DictWriter(csvfile, fieldnames=veldnamen, delimiter=';')

    schrijver.writeheader()
    for item in inkomsten:
        schrijver.writerow({"Product":item, "Opbrengst":inkomsten[item]})

