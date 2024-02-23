def peso_nota(A, PA, B, PB):
    media = (A * PA + B * PB) / (PA + PB)
    return media

A = float(input())
PA = 3.5

B = float(input())
PB = 7.5

media = peso_nota(A, PA, B, PB)

print("MEDIA = {:.5f}".format(media))
