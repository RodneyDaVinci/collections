dagen = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]

dageninput = input("Welke dagen van de week wilt u zien? Alle dagen(a), Werkdagen(b), Weekenddagen(c), Alle dagen omgekeerd(d,) Werkdagen omgekeerd(e) of Weekenddagen omgekeerd(f): ")

# Alle dagen
if dageninput == "a":
    for a in range(len(dagen)):
        print(dagen[a])

# Werkdagen
if dageninput == "b":
    for b in dagen[:-2]:
        print(b)

# Weekenddagen
if dageninput == "c":
    print(dagen[5])
    print(dagen[6])

# Alle dagen omgekeerd
if dageninput == "d":
    for d in reversed(dagen):
        print(d)

# Werkdagen omgekeerd
if dageninput == "e":
    for e in reversed(dagen[:-2]):
        print(e)

# Weekenddagen omgekeerd
if dageninput == "f":
    print(dagen[-1])
    print(dagen[-2])



