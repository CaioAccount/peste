inicio = int(input("digite o inicio do intervalo: "))
fim = int(input("digite o fim do intervalo: "))
n = inicio

while n <= fim:
    soma = 0
    x = 1
    while x < n:
        soma += x * (n % x == 0)
        x += 1
    k = 0
    while k < (soma == n):
        print(n)
        k += 1
    n += 1