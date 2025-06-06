from gerenciador_tarefas import auth, tasks

def main():
    print("Bem-vindo ao Gerenciador de Tarefas!")
    user = None

    while not user:
        action = input("Você deseja (1) Entrar ou (2) Registrar? ")
        if action == "1":
            username = input("Usuário: ")
            password = input("Senha: ")
            if auth.login(username, password):
                print("Login bem-sucedido!")
                user = username
            else:
                print("Usuário ou senha incorretos.")
        elif action == "2":
            username = input("Novo usuário: ")
            password = input("Nova senha: ")
            success, message = auth.register(username, password)
            print(message)
            if success:
                user = username

    while True:
        print("\nMENU:")
        print("1. Adicionar Tarefa")
        print("2. Ver Tarefas")
        print("3. Remover Tarefa")
        print("4. Editar Tarefa")
        print("5. Marcar/Desmarcar como Concluída")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite a tarefa: ")
            tasks.add_task(user, task)
            print("Tarefa adicionada.")
        elif choice == "2":
            user_tasks = tasks.get_tasks(user)
            if not user_tasks:
                print("Nenhuma tarefa encontrada.")
            for i, t in enumerate(user_tasks):
                status = "✔️" if t.get("concluida") else "❌"
                print(f"{i}. {status} {t['descricao']}")
        elif choice == "3":
            index = int(input("Digite o índice da tarefa a remover: "))
            tasks.remove_task(user, index)
            print("Tarefa removida.")
        elif choice == "4":
            index = int(input("Digite o índice da tarefa a editar: "))
            nova = input("Digite a nova descrição: ")
            tasks.edit_task(user, index, nova)
            print("Tarefa editada.")
        elif choice == "5":
            index = int(input("Digite o índice da tarefa: "))
            tasks.alternar_conclusao(user, index)
            print("Status da tarefa alterado.")
        elif choice == "6":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
