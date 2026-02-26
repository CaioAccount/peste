n = int(input("digite um numero inteiro: "))
soma = 0

for x in range(1, n):
    soma += x * (n % x == 0)
print("é um número perfeito" * (soma == n) +
      "não é um número perfeito" * (soma != n))