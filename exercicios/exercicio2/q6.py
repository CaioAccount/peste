n = int(input("digite um número de 4 dígitos: "))
if 1000 <= n <= 9999:
    d4 = n % 10
    d3 = (n // 10) % 10
    d2 = (n // 100) % 10
    d1 = n // 1000
    if (d1 == d2 or d1 == d3 or d1 == d4 or d2 == d3 or d2 == d4 or d3 == d4):
        print(f"o número {n} tem dígitos repetidos")
    else:
        print(f"o número {n} tem todos os dígitos diferentes")
elif -9999 <= n <= -1000:
    print("digite um número positivo")
else:
    print("o número não tem 4 dígitos")