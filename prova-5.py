# Taismara de Souza Bento RA: 0220482532001

print("Taismara de Souza Bento")
print("RA: 0220482532001")

q = int(input("Quantidade de itens produzidos: "))
d = float(input("Percentual de defeitos (ex: 0.05 para 5%): "))
defeito = float(q * d)

C_inicial = 1000
F_comp = 1.15

if q > 1000 and C_inicial > 500:
    F_comp = 1.15
else:
    F_comp = 1.10

C_corrigido = C_inicial * F_comp


dias = int(input("Informe o número de dias com defeitos registrados: "))

if defeito > 10 or dias > 5:
    print("Penalidade Alta: 2% redução no lucro.")
    C_final = C_corrigido * 0.98
elif 0.05 <= defeito <= 0.10 and dias > 0:
    print("Penalidade Média: 1% redução no lucro.")
    C_final = C_corrigido * 0.99
else:
    print("Sem penalidade. Custo final apenas com correção.")
    C_final = C_corrigido

print(f"Custo Base Corrigido: R$ {C_corrigido:.2f}")
print(f"Custo Final do item: R$ {C_final:.2f}")
