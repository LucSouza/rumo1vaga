print("""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.""")

nInt1 = int(input("Informe um numero inteiro: "))
nInt2 = int(input("Informe outro inteiro: "))
nReal = float(input("Informe um numero real: "))

calc1 = float((nInt1*2) * (nInt2/2))
calc2 = float((nInt1*3) + nReal)
calc3 = float(nReal**3)
print(f"o produto do dobro de {nInt1} com metade de {nInt2}: {calc1}")
print(f"a soma do triplo de {nInt1} com {nReal}: {calc2}")
print(f"{nReal} elevado ao cubo: {calc3:.2f}")
