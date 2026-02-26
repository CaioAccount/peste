quant = 0

for n in range(1, 201):
    divisores = 0
    for x in range(1, n + 1):
        divisores += (n % x == 0)
    quant += (divisores == 2)

print(f"quantidade de números primos: {quant}")