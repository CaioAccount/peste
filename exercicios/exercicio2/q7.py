n = int(input("digite um número de quatro dígitos: "))
if 1000 <= n <= 9999:
    primeiros_dois = n // 100 
    ultimos_dois = n % 100 
    dezena_final = ultimos_dois // 10
    unidade_final = ultimos_dois % 10
    ultimos_dois_invertidos = (unidade_final * 10) + dezena_final
    if primeiros_dois == ultimos_dois_invertidos:
        print(f"o número {n} é um número espelho")
    else:
        print(f"o número {n} NÃO é um número espelho")
        
elif 0 <= n <= 999:
    print("o número inserido tem menos de quatro dígitos")
else:
    print("o número inserido tem mais de quatro dígitos ou é negativo")