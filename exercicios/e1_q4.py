hora_atual = int(input("hora atual: "))
horas_espera = int(input("horas até o alarme: "))

hora_alarme = (hora_atual + horas_espera) % 24
print(f"o alarme tocará às {hora_alarme} horas")