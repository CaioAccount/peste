num = int(input("digite um número inteiro: "))
if num % 4 == 0 and num % 5 == 0:
    print("divisível por 4 e por 5")
elif num % 5 == 0:
    print("divisível por 5")
elif num % 4 == 0:
    print("divisível por 4")
else:
    print("não é divisível por 4 ou 5")