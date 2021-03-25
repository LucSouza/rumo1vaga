print("""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. """)

print("Calculo de multa por excesso de peso")
peso = float(input("Informe o peso de peixes: "))

vMulta = float(4)
limite = 50

if peso > limite:
  excesso = peso - limite
  multa = excesso * vMulta
  print(f"O excesso foi de : {excesso}kg, gerando uma multa de: R$ {multa:.2f}")
else:
  print(f"{peso} não supera o limite de 50 kg diarios")
