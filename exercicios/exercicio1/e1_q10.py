numero = int(input("digite um número de 5 dígitos: "))

soma = 0

soma += numero // 10000
numero %= 10000

soma += numero // 1000
numero %= 1000

soma += numero // 100
numero %= 100

soma += numero // 10
numero %= 10

soma += numero

print(f"soma dos dígitos: {soma}")
