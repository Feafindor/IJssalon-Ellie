def presenteer(dictionary, totaal):
#inleidende tekst
    print("\ninvoer: \n")
    print(dictionary)
    print("\nuitvoer: \n")

# weergave per item
    for k,v in dictionary.items():
        print(f"{k}: {v}")

# totaal weergeven
    print("\n" + 20*"=")
    print(f"\nTotaal: {totaal}")
    return "" #zonder return zou er None worden weergegeven dus

#alternatief: gebruik niet print maar gebruik return om een string terug te geven

def presenteer2(dictionary, totaal):
    output = "\ninvoer: \n\n"
    output += str(dictionary)
    output += "\n\nuitvoer: \n\n"
    for k,v in dictionary.items():
        output += f"{k}: {v}\n"
    output += "\n" + 20*"=" + "\n"
    output += f"\nTotaal: {totaal}\n"
    return output

    