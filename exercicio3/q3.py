soma = 0
quant = 0

num = int(input("digite um numero (-1 para encerrar): "))

while num != -1:
    soma += num
    quant += 1
    num = int(input("digite um numero (-1 para encerrar): "))

print(f"media: {soma / quant}")