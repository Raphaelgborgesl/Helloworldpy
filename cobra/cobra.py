def criar_arquivo_txt(nome_arquivo, texto):
	with open(nome_arquivo, 'w') as arquivo:
		arquivo.write(texto)

import os
import time
       
# Solicita o nome de usuário
nome_usuario = input("Digite seu nome de usuário: ")

# Verifica se o nome de usuário é Raphael
if nome_usuario == "Raphael":
    # Solicita a senha
    senha = input("Digite sua senha: ")

    # Verifica se a senha está correta
    if senha == "boto":
        print("Acesso concedido.")
        # Simula a digitação de "Parabens Raphael"
        # pyautogui.write("Parabens "+ nome_usuario, interval=0.1)
        criar_arquivo_txt("rambo.txt", "Desce a rola")
    else:
        print("Senha incorreta.")
else:
    print("Nome de usuário incorreto.")