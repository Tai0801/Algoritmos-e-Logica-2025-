# Taismara de Souza Bento RA: 022048252801
print("Taismara de Souza Bento")
print("RA: 022048252801")

P = float(input("Informe o valor do investimento inicial: "))
T = int(input("Informe o prazo do investimento em meses: "))

if T < 6:
    J = 0.08
elif 6 <= T <= 12:
    J = 0.12
else:
    J = 0.18

rendimento_total = P * J * T

print(f"A taxa de juros foi aplicada de R${J*100:.2f} ao mês")
print(f"O rendimento total foi de R$ {rendimento_total:.2f}")
