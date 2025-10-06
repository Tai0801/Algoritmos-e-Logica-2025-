# Taismara de Souza Bento RA: 0220482532001

print("Taismara de Souza Bento")
print("RA: 0220482532001")

pureza = float(input("Informe a pureza do lote (ex: 0.95 para 95%): "))
massa_total = float(input("Informe a massa total do lote (em kg): "))
taxa_contaminacao = float(input("Informe a taxa de contaminacao (ex: 0.02 para 2%): "))

if (pureza > 0.98) and (taxa_contaminacao <= 0.01):
    classificacao = "VENDA IMEDIATA (Margem Máxima)"
    base = 1.10
elif (pureza < 0.90) or (taxa_contaminacao > 0.05):
    classificacao = "DESCARTE OU RE-PROCESSAMENTO"
    base = 0.00
else:
    classificacao = "ACEITÁVEL (Margem Mínima)"
    base = 0.90

preco_final = massa_total * pureza * base

print("Classificação do lote:", classificacao)
print("Preço final: R$", preco_final)
