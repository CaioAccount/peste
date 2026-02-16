p = 32.90
d = 0.35
q = 75

p_desc = p * (1 - d)
transporte = 4.00 + (q - 1) * 0.80
total = p_desc * q + transporte
print("custo total:", round(total, 2))