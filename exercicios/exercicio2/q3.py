numero = int(input("digite um numero inteiro: "))

if 50 <= numero <= 100:
    print("entre 50 e 100")
else:
    print("menor que 0 ou maior que 200") if numero < 0 or numero > 200 else print("fora das condições anteriores")