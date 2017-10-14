def code(invoerstring):
    cd = ""
    lijst = []
    for x in invoerstring:
        c = chr((ord(x) + 3))
        lijst.append(c)

    for y in range(len(lijst)):
        cd = cd + lijst[y]
    return cd


print(code(input()))
