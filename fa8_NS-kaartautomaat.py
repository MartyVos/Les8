def inlezen_beginstation(stations):
    while 1:
        start = input("Geef uw beginstation: ")
        if start in stations:
            return start
        else:
            print("Deze trein komt niet in", start)


def inlezen_eindstation(stations, beginstation):
    while 1:
        eindstation = input("Geef uw eindstation: ")
        if eindstation in stations and stations.index(eindstation) > stations.index(beginstation):
            return eindstation
        elif eindstation not in stations:
            print("Deze trein komt niet in", eindstation)


def omroepen_reis(stations, beginstation, eindstation):
    begin = stations.index(beginstation) + 1
    eind = stations.index(eindstation) + 1
    afstand = eind - begin
    prijs = afstand * 5

    print("Het beginstation", beginstation, "is het", str(begin) + "e", "station in het traject.")
    print("Het eindstation", eindstation, "is het", str(eind) + "e", "station in het traject.")
    print("De afstand bedraagt", afstand, "station(s).")
    print("De prijs van het kaartje is", prijs, "euro")

    print("\nU stapt in de trein in:", beginstation)
    for x in range(len(stations)):
        if stations.index(beginstation) < x < stations.index(eindstation):
            print("  - ", stations[x])
    print("U stapt uit in:", eindstation)


stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht"]

a = inlezen_beginstation(stations)
b = inlezen_eindstation(stations, a)
omroepen_reis(stations, a, b)
