import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return {}
    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_tarefas(todas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(todas, f, ensure_ascii=False, indent=2)

def add_task(usuario, descricao):
    todas = carregar_tarefas()
    if usuario not in todas:
        todas[usuario] = []
    todas[usuario].append({"descricao": descricao, "concluida": False})
    salvar_tarefas(todas)

def get_tasks(usuario):
    todas = carregar_tarefas()
    return todas.get(usuario, [])

def remove_task(usuario, indice):
    todas = carregar_tarefas()
    if usuario in todas and 0 <= indice < len(todas[usuario]):
        del todas[usuario][indice]
        salvar_tarefas(todas)

def edit_task(usuario, indice, nova_descricao):
    todas = carregar_tarefas()
    if usuario in todas and 0 <= indice < len(todas[usuario]):
        todas[usuario][indice]["descricao"] = nova_descricao
        salvar_tarefas(todas)

def alternar_conclusao(usuario, indice):
    todas = carregar_tarefas()
    if usuario in todas and 0 <= indice < len(todas[usuario]):
        todas[usuario][indice]["concluida"] = not todas[usuario][indice]["concluida"]
        salvar_tarefas(todas)
