ver = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                  4, 4, 4, 2, 2, 2, 2]

dicti = dict()

for say in ver:
    if say not in dicti:
        dicti.__setitem__(say, 1)
    else:
        dicti[say] = dicti[say] + 1

for say in sorted(dicti.keys()):
    print(say, ":", dicti[say])
