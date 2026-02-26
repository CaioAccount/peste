num = int(input("digite um número inteiro: "))
soma = 0

for x in range(1, num):
    soma += x * ((x % 4 == 0) or (x % 6 == 0))
print(f"somatória: {soma}")