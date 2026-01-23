def decoreer(tekst=""):
    lengte=len(tekst)+4
    print()
    print(lengte*"*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
    try:
        bedrag_pp=bedrag/personen
        round(bedrag_pp, 2)
    except:
        bedrag_pp="??"
    return f"Het bedrag per persoon is {bedrag_pp:.2f}"

b=int(input("Welk bedrag zit er in de fooienpot? "))
p=int(input("Over hoeveel mensen moet de pot verdeeld worden? "))
print(fooi_pp(b,p))
