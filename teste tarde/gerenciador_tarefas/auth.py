import json
import os

ARQUIVO_USUARIOS = "usuarios.json"

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_usuarios(dados):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def register(username, password):
    usuarios = carregar_usuarios()
    if username in usuarios:
        return False, "Usuário já existe."
    usuarios[username] = password
    salvar_usuarios(usuarios)
    return True, "Usuário registrado com sucesso!"

def login(username, password):
    usuarios = carregar_usuarios()
    return usuarios.get(username) == password
