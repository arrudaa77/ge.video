import json
from videos import filme_existe


def carregar_tudo():
    try:
        with open("dados.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"usuarios": [], "videos": []}


def salvar_tudo(dados):
    with open("dados.json", "w") as f:
        json.dump(dados, f, indent=4)
    print("Dados sincronizados com sucesso!")


def adicionar_favorito(dados, usuario, id_video):
    if not filme_existe(dados, id_video):
        print("❌ Filme não encontrado.")
        return

    for u in dados["usuarios"]:
        if u["nome"] == usuario:
            if id_video not in u["favoritos"]:
                u["favoritos"].append(id_video)
                print("Adicionado aos favoritos!")
            else:
                print("Esse filme já está nos seus favoritos.")
            return


def remover_favorito(dados, usuario, id_video):
    if not filme_existe(dados, id_video):
        print("❌ Filme não encontrado.")
        return

    for u in dados["usuarios"]:
        if u["nome"] == usuario:
            if id_video in u["favoritos"]:
                u["favoritos"].remove(id_video)
                print("Removido dos favoritos!")
            else:
                print("Este filme não estava nos favoritos.")
            return


def criar_playlist(dados, usuario, nome_playlist):
    for u in dados["usuarios"]:
        if u["nome"] == usuario:
            if nome_playlist not in u["playlists"]:
                u["playlists"][nome_playlist] = []
                print(f"Playlist '{nome_playlist}' criada!")
            else:
                print("Você já tem uma playlist com esse nome.")
            return


def adicionar_na_playlist(dados, usuario, nome_playlist, id_video):
    if not filme_existe(dados, id_video):
        print("❌ Filme não encontrado.")
        return

    for u in dados["usuarios"]:
        if u["nome"] == usuario:
            if nome_playlist not in u["playlists"]:
                print("❌ Playlist não encontrada.")
                return

            if id_video not in u["playlists"][nome_playlist]:
                u["playlists"][nome_playlist].append(id_video)
                print(f"Filme adicionado à playlist '{nome_playlist}'.")
            else:
                print("O filme já está nessa playlist.")
            return


def remover_da_playlist(dados, usuario, nome_playlist, id_video):
    if not filme_existe(dados, id_video):
        print("❌ Filme não encontrado.")
        return

    for u in dados["usuarios"]:
        if u["nome"] == usuario:
            if nome_playlist not in u["playlists"]:
                print("❌ Playlist não encontrada.")
                return

            if id_video in u["playlists"][nome_playlist]:
                u["playlists"][nome_playlist].remove(id_video)
                print(f"Filme removido da playlist '{nome_playlist}'.")
            else:
                print("O filme não está nessa playlist.")
            return

def estatisticas(dados):
    print("\n=== ESTATÍSTICAS ===")
    print(f"Total de usuários: {len(dados['usuarios'])}")
    print(f"Total de filmes: {len(dados['videos'])}")

    top = sorted(dados["videos"], key=lambda x: x["curtidas"], reverse=True)[:5]
    print("\nTop 5 filmes mais curtidos:")
    for v in top:
        print(f" - {v['nome']}: {v['curtidas']} curtidas")