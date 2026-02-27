inicio = int(input("digite o início do intervalo: "))
fim = int(input("digite o fim do intervalo: "))

for n in range(inicio, fim + 1):
    qtd_digitos = 0
    for x in str(n):
        qtd_digitos += 1
    soma = 0
    for digito in str(n):
        soma += int(digito) ** qtd_digitos
    for x in range(soma == n):
        print(n)