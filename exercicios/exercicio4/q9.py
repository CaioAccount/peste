inicio = int(input("digite o início do intervalo: "))
fim = int(input("digite o fim do intervalo: "))

for n in range(inicio, fim + 1):
    numero_str = str(n)
    qtd_digitos = len(numero_str)
    
    soma = 0
    for digito in numero_str:
        soma += int(digito) ** qtd_digitos
    
    for x in range(soma == n):
        print(n)