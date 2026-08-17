def buscar_filme(dados, nome):
    nome_busca = nome.lower()
    return [v for v in dados["videos"] if nome_busca in v["nome"].lower()]


def listar_filmes(dados):
    print("\n=== LISTA DE FILMES ===")
    for v in dados["videos"]:
        print(f'ID: {v["id"]} | Nome: {v["nome"]} | Curtidas: {v["curtidas"]}')


def filme_existe(dados, id_video):
    for v in dados["videos"]:
        if v["id"] == id_video:
            return True
    return False


def curtir_filme(dados, id_video):
    if not filme_existe(dados, id_video):
        print("❌ Filme não encontrado.")
        return

    for v in dados["videos"]:
        if v["id"] == id_video:
            v["curtidas"] += 1
            print("O filme foi curtido! Boa!")
            return


def descurtir_filme(dados, id_video):
    if not filme_existe(dados, id_video):
        print("❌ Filme não encontrado.")
        return

    for v in dados["videos"]:
        if v["id"] == id_video:
            if v["curtidas"] > 0:
                v["curtidas"] -= 1
                print("Curtida removida! Que pena...")
            else:
                print("Este filme já tem 0 curtidas.")
            return


def adicionar_filme(dados, nome_video):
    novo_id = max([v["id"] for v in dados["videos"]], default=0) + 1
    dados["videos"].append({"id": novo_id, "nome": nome_video, "curtidas": 0})
    print(f"Filme '{nome_video}' cadastrado com ID {novo_id}!")


def excluir_filme(dados, id_video):
    if not filme_existe(dados, id_video):
        print("ID não encontrado.")
        return

    dados["videos"] = [v for v in dados["videos"] if v["id"] != id_video]
    print("Esse filme foi removido!")