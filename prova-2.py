# Taismara de Souza Bento RA: 0220482528001

print("Taismara de Souza Bento")
print("RA: 0220482528001")

print("***************")

glicose = float(input("Informe o nível de glicose no sangue em jejum: "))

if glicose < 100:
    print("Glicemia Normal")
elif glicose >= 100 and glicose <= 125:
    print("Glicemia Alterada: Avaliar com profissional de saúde")
else:
    print("Diabetes: Nível Alto")
