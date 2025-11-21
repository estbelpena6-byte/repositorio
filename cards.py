cards = ['4242424242424242','4000056655665556','5555555555554444','378282246310005','6011111111111117']

"""
si la tc comienza con 4, mostrar 4 primeros, 8x y 4 ultimos
si comienza con 5, mostrar 6 primeros, 6xx y ultimos 4
si comienza con 3, igual que el cinco
si comienza con 6, mostrar primeros 4, 6x y ultimos 6
"""

for x in cards:
    maskedCard = ""
    if x.startswith("4"):
        maskedCard = x[:4] + "x"*8 + x[-4]
    else:
        continue
    print(maskedCard)

for x in cards:
    maskedCard = ""
    if x.startswith("5"):
        maskedCard = x[:6] + "x"*6 + x[-4]
    else:
        continue
    print(maskedCard)

for x in cards:
    maskedCard = ""
    if x.startswith("3"):
        maskedCard = x[:6] + "x"*6 + x[-4]
    else:
        continue
    print(maskedCard)

for x in cards:
    maskedCard = ""
    if x.startswith("6"):
        maskedCard = x[:4] + "x"*6 + x[-6]
    else:
        continue
    print(maskedCard)    

