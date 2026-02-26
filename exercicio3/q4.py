num = int(input("digite um numero (0 para encerrar): "))

while num != 0:
    m = num
    while m < 100:
        print(m)
        m += num
    
    num = int(input("digite um numero (0 para encerrar): "))