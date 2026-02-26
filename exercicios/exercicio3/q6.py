import random

num = random.randint(10,50)

palpite = int(input("adivinhe o número entre 10 e 50: "))

while palpite != num:
    print("o número secreto é maior" * (palpite < num) + 
          "o número secreto é menor" * (palpite > num))
    palpite = int(input("tente novamente: "))
print("acertou")