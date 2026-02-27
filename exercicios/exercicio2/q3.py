num = int(input("digite um numero inteiro: "))

if 50 <= num <= 100:
    print("entre 50 e 100")
elif num < 0 or num > 200:
    print("menor que 0 ou maior que 200")
else:
    print("fora das condições anteriores")