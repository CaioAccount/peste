num = int(input("digite um número inteiro positivo: "))
prod = 1

for i in range(1, num + 1):
    prod *= i

print(f"o produto acumulado de 1 até {num} é: {prod}")