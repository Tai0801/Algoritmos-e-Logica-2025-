# Taismara de Souza Bento RA: 0220482532001

print("Taismara de Souza Bento")
print("RA: 0220482532001")


peso = float(input("Informe o peso da encomenda em kilos: "))
distancia = float(input("Informe a distancia em km: "))

custo_base = peso * 1.5 + distancia * 0.25

custo_final = custo_base

if custo_base > 200:
    custo_final = custo_base * 0.90
    print("Desconto aplicado!")
elif 50 <= custo_base <= 200:
    print("Não tem direito ao desconto.")
else:
    custo_final = custo_base + 5
    print("Taxa adicional de R$5,00 aplicada.")

print(f"O custo base original foi de R$: {custo_base:.2f}")
print(f"O custo final foi de R$: {custo_final:.2f}")
