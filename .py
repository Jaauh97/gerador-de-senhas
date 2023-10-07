#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç','`', '/', '|', 'ª', 'º', '¿',]

print("Bem Vindo Ao Gerador de Senhas!")
# quantas letras quer em sua senha?
nr_letters= int(input("Quantas Letras Voce Gostaria de ter em Sua Senha?\n")) 
# quantos simbolos quer em sua senha?
nr_symbols = int(input(f"Quantos Simbolos Voce Gostaria de ter em Sua Senha ?\n"))
# quantos numeros quem em sua senha?
nr_numbers = int(input(f"Quantos Numeros Voce gostaria de ter em sua senha? \n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):10
  password_list += random.choice(numbers)

# print(password_list)
  random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Sua nova senha: {password}")

import time
time.sleep(60)