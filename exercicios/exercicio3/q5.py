n = int(input("digite um numero: "))

fat = 1
cont = 1

while cont <= n:
    fat *= cont
    cont += 1
print(f"fatorial de {n} é {fat}")