num = float(input("digite um numero decimal: "))
binario = ""

while num > 0:
    binario = str(num % 2) + binario
    num = num // 2
while len(binario) == 0:
    binario = "0"
print(f"binário: {binario}")