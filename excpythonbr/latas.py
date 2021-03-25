print("""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. """)

areaPintar = float(input("Qual o tamanho da area a ser pintada em mts quadrados?: "))

cobertura = areaPintar / 3
umaLata = 18
latas = 1
precoLata = 80
while cobertura > umaLata:
  latas = latas +1
  cobertura = cobertura - umaLata

print(f"Você precisara {latas} lata/s de tinta para cobrir a area de {areaPintar}mts quadrados, o custo total será de {latas * precoLata}")
