num = int(input("digite um numero inteiro: "))
soma = 0

for i in range(num):
    soma += i * (i % 3 == 0)
print(f"a soma dos multiplos de 3 de 0 até {num} é: {soma}")