num = int(input("digite um numero inteiro: "))

if num >= 50 and num <= 100:
    print("entre 50 e 100")
if num < 0 or num > 200:
    print("menor que 0 ou maior que 200")
if num < 50 and num > 0 or num > 100 and num < 200:
    print("fora das condições anteriores")