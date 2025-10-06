# Taismara de Souza Bento RA: 0220482532001

print("Taismara de Souza Bento")
print("RA: 0220482532001")

preco_de_custo = float(input("Informe o preço de custo: "))
preco_de_venda = float(input("Informe o preço de venda: "))

lucro = preco_de_venda - preco_de_custo
margem = lucro / preco_de_custo * 100

if margem > 30:
    print("Margem: Excelente.")
elif margem >= 10 and margem <= 30:
    print("Margem: Satisfatória.")
else:
    print("Margem Baixa: Avaliar preço de venda.")
