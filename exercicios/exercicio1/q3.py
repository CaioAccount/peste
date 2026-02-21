hora_atual = 9
horas_espera = 37

hora_alarme = (hora_atual + horas_espera) % 24
print(f"o alarme tocará às {hora_alarme} horas")