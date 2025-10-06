# Taismara de Souza Bento RA: 0220482532001

print("Taismara de Souza Bento")
print("RA: 0220482532001")

livre = float(input("Digite a taxa livre de risco: "))
Sigma = float(input("Digite o desvio-padrão da volatilidade(%): ")) / 100

if Sigma == 0:
    print("Erro: o desvio-padrão (Sigma) não pode ser zero.")
else:
    R_investimento = 0.18
    R_livre = livre
    Sigma = Sigma

    Spread = R_investimento - R_livre
    Sharpe = Spread / Sigma

    if Sharpe >= 1:
        classificacao = "Investimento Excelente: Alta performance ajustada ao risco."
    elif Sharpe >= 0.5:
        classificacao = "Investimento Aceitável: Retorno positivo, mas os riscos são consideráveis."
    else:
        classificacao = "Investimento Ruim: Risco elevado em relação ao retorno."

    print(f"\nSharpe Ratio: {Sharpe:.2f}")
    print(f"Classificação: {classificacao}")
