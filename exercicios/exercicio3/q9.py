num = int(input("digite um número: "))
soma = 0
x = 1

while x < num:
    soma += x * (num % x == 0)
    x += 1
print(soma == num)