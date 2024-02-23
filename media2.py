def peso_nota(A, PA, B, PB, C, PC):
    media = (A * PA + B * PB + C * PC) / (PA + PB + PC)
    return media

A = float(input())
PA = 2

B = float(input())
PB = 3

C = float(input())
PC = 5

media = peso_nota(A, PA, B, PB, C, PC)

print("MEDIA = {:.1f}".format(media))
