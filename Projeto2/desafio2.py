def ranking (vitorias, derrotas):
    
    saldoVitorias = vitorias - derrotas

    return saldoVitorias


vitorias = int(input("Informe o número de vitórias: "))

derrotas = int(input("Informe o número de derrotas: "))

if vitorias <= 10:
    nivel = "Ferro"
elif vitorias <= 20:
    nivel = "Bronze"
elif vitorias <= 50:
    nivel = "Prata"
elif vitorias <= 80:
    nivel = "Ouro"
elif vitorias <= 90:
    nivel = "Diamante"
elif vitorias <= 100:
    nivel = "Lendário"
else:
    nivel = "Imortal"



saldoVitorias = ranking(vitorias, derrotas)

print(f"O Herói tem de saldo de {saldoVitorias} e está no nível de {nivel}.")