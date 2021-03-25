print("Em base a sua altura calculamos seu peso ideal")
alt = float(input("Informe sua altura: "))
sexo = int(input("Informe 1 se for homem ou 2 se for mulher:"))

if sexo == 1:
  pesoIdeal = float((72.7 * alt) - 58)
else:
  pesoIdeal = float((62.1 * alt) - 44.7)


print(f"Basado na sua altura '{alt}', seu peso ideal é: {pesoIdeal:.2f}'")
