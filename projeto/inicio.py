import os

def projeto():
        print("Boas-vindas a FeiFlix! \n\n")
        print("Digite 1 para se cadastrar; \n") 
        print("Digite 2 para realizar login; \n")
        print("Digite 0 para sair. \n")

projeto()

c = int(input("Comando: "))
if c == 1:
    usuario_cadastrado = str(input("Digite o novo usuário: "))
    senha_cadastrada = int(input("Digite a nova senha: "))

arquivo = open ("usuarios.txt", "a")