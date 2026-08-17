import subprocess
import os

def limpar_tela():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell = True)

from usuarios import cadastrar_usuario, login, listar_usuarios
from videos import (buscar_filme, listar_filmes, curtir_filme, descurtir_filme, adicionar_filme, excluir_filme)
from sistema import (carregar_tudo, salvar_tudo, adicionar_favorito, remover_favorito, criar_playlist, adicionar_na_playlist, remover_da_playlist, estatisticas)

dados = carregar_tudo()
usuario_logado = None

while True:
    limpar_tela()
    print("Oi! Bem-vindo ao GE Video!")
    
    if not usuario_logado:
        print("\n1 - Cadastrar | 2 - Login | 0 - Sair")
    
    if usuario_logado:
        print(f"\nVocê está logado como {usuario_logado['nome']}")
    
    if usuario_logado:
        print("\n3 - Buscar    | 4 - Listar")
        print("5 - Curtir    | 6 - Descurtir")
        print("7 - Favoritar | 8 - Remover Favorito")
        print("9 - Criar Playlist | 10 - Adicionar na Playlist")
        print("11 - Remover da Playlist | 0 - Sair")
        
        if usuario_logado.get("admin"):
            print("\n[ADMIN] I - Adicionar Filme | II - Excluir Filme")
            print("III - Estatísticas | IV - Usuários")

    op = input("\nEscolha o que você deseja: ").strip().upper()

    if op == "1":
        nome = input("Nome: ").strip()
        senha = input("Senha: ").strip()
        
        if not nome or not senha:
            print("\nLembre-se: o seu nome e a sua senha não podem ficar em branco!")
        else:
            if cadastrar_usuario(dados, nome, senha):
                salvar_tudo(dados)
        
        input("\nPressione Enter para continuar...")

    elif op == "2":
        nome = input("Nome: ").strip()
        senha = input("Senha: ").strip()
        
        if not nome or not senha:
            print("\nLembre-se: o seu nome e a sua senha não podem ficar em branco!")
        else:
            usuario_logado = login(dados, nome, senha)
            
        input("\nPressione Enter para continuar...")

    elif op in ["3", "4", "5", "6", "7", "8", "9", "10","11"]:
        if not usuario_logado:
            print("Faça login primeiro, acalme-se!")
            input()
            continue
        
        try:
            if op == "3":
                nome_busca = input("Nome do filme: ")
                vids = buscar_filme(dados, nome_busca)
                if vids:
                    print("\n=== RESULTADOS ENCONTRADOS ===")
                    for v in vids:
                        print(f"ID: {v['id']} | {v['nome']} ({v['curtidas']} curtidas)")
                else:
                        print("\n[!] Nenhum filme encontrado, que pena!")
                input("\nPressione Enter para voltar...")

            elif op == "4":
                listar_filmes(dados)
                input("\nPressione Enter para voltar...")
            
            if op == "5":
                idv = int(input("ID do filme: "))
                curtir_filme(dados, idv)
                input("\nPressione Enter para voltar...")

            elif op == "6":
                idv = int(input("ID do filme: "))
                descurtir_filme(dados, idv)
                input("\nPressione Enter para voltar...")

            elif op == "7":
                idv = int(input("ID do filme: "))
                adicionar_favorito(dados, usuario_logado["nome"], idv)
                input("\nPressione Enter para voltar...")
            
            elif op == "8":
                idv = int(input("ID do filme: "))
                remover_favorito(dados, usuario_logado["nome"], idv)
                input("\nPressione Enter para voltar...")
            
            elif op == "9":
                nomep = input("Nome da sua nova playlist: ")
                criar_playlist(dados, usuario_logado["nome"], nomep)
                input("\nPressione Enter para voltar...")
            
            elif op == "10":
                nomep = input("Nome da playlist destino: ")
                idv = int(input("ID do filme: "))
                adicionar_na_playlist(dados, usuario_logado["nome"], nomep, idv)
                input("\nPressione Enter para voltar...")

            elif op == "11":
                nomep = input("Nome da playlist: ")
                idv = int(input("ID do filme: "))
                remover_da_playlist(dados, usuario_logado["nome"], nomep, idv)
                input("\nPressione Enter para voltar...")
            salvar_tudo(dados)
        
        except ValueError:
            print("Digite apenas números para IDs!")
            print("Por favor, use apenas os (IDs) que aparecem em 4 - Listar.")
            input("\nPressione Enter para tentar novamente...")

    elif op == "I":
        if usuario_logado and usuario_logado.get("admin"):
            nome_vid = input("Nome do filme: ").strip()
            if not nome_vid:
                print("Lembre-se de identificar o filme com um nome!")
            else:
                adicionar_filme(dados, nome_vid)
        else:
            print("Apenas admins podem fazer isso!")
        input("\nPressione Enter para continuar...")

    elif op == "II":
        if usuario_logado and usuario_logado.get("admin"):
            try:
                idv = int(input("ID para excluir: "))
                excluir_filme(dados, idv)
            except ValueError:
                print("Esse ID é inválido.")
        else:
            print("Apenas admins podem fazer isso!")
        input("\nPressione Enter para continuar...")

    elif op == "III":
        if usuario_logado and usuario_logado.get("admin"):
            estatisticas(dados)
        else:
            print("Apenas admins podem ver estatísticas!")
        input("\nPressione Enter para continuar...")

    elif op == "IV":
        if usuario_logado and usuario_logado.get("admin"):
            listar_usuarios(dados)
        else:
            print("Apenas admins podem fazer isso!")
        input("\nPressione Enter para continuar...")

    elif op == "0":
        print("Salvando seus dados. Obrigado por colaborar com a gente! Até a próxima!")
        input("\nPressione Enter para continuar...")
        salvar_tudo(dados)
        break

    else:
        print("Opção inválida!")
        input("\nPressione Enter para voltar...")