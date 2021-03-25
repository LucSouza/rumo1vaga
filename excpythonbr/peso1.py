print("Em base a sua altura calculamos seu peso ideal")
alt = float(input("Informe sua altura: "))


pesoIdeal = float((72.7 * alt) - 58)

print(f"Basado na sua altura '{alt}', seu peso ideal é: {pesoIdeal:.2f}")
