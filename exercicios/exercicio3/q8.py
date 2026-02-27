num = float(input("digite um numero decimal: "))
binario = "0"

while num > 0:
    binario = ""
    while num > 0:
        binario = str(num % 2) + binario
        num = num // 2
print(f"binário: {binario}")