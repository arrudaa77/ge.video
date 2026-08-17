import json

def cadastrar_usuario(dados, nome, senha):
    for u in dados["usuarios"]:
        if u["nome"] == nome:
            print("O usuário já existe!")
            return False

    novo = {
        "nome": nome,
        "senha": senha,
        "favoritos": [],
        "playlists": {},
        "admin": False
    }

    dados["usuarios"].append(novo)
    print(f"Conta criada com sucesso! Aproveite! Usuário: {nome}")
    return True


def login(dados, nome, senha):
    for u in dados["usuarios"]:
        if u["nome"] == nome and u["senha"] == senha:
            print(f"Login efetuado com sucesso! Bem-vindo, {nome}.")
            return u

    print("Usuário ou senha inválidos! Tente novamente.")
    return None

def listar_usuarios(dados):
    print("\n=== LISTA DE USUÁRIOS ===")
    for u in dados["usuarios"]:
        tipo = "Admin" if u.get("admin") else "Membro"
        print(f"Nome: {u['nome']} | Tipo: {tipo} | Favoritos: {len(u['favoritos'])} | Playlists: {len(u['playlists'])}")