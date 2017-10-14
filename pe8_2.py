import random


def monopolyworp():
    x = 0
    while 1:
        input()
        a = random.randrange(1, 7)
        b = random.randrange(1, 7)

        if a == b:
            x += 1
            if x == 3:
                print(a, "+", b, "=", a + b, "(direct naar de gevangenis)")
                break
            print(a, "+", b, "=", a + b, "(dubbel)")
        else:
            print(a, "+", b, "=", a + b)


monopolyworp()
