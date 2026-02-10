tarefas = []

def mostrar():
    print("OPÇÔES")
    print("1 - Adicionar Tarefas")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefas")
    print("0 - Sair")


while True:
    mostrar()
    try:
        opcao = int(input("Digite sua opção: "))
        
    except ValueError:
        print("Por favor, utilize apenas números válidos")
        continue
    

    if opcao == 0:
        print("Saindo do Programa...")
        break
    
    elif opcao == 1:
        registro = int(input("Digite quantas tarefas deseja registrar: "))
        for r in range(registro):
            titulo = input("Digite o título da Tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")

            tarefa = {
                "Titulo":titulo,
                "Descrição":descricao
            }

            tarefas.append(tarefa)
            print("Tarefa adicionada!")

    elif opcao == 2:
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1} - {tarefa['Titulo']}")
                print(f" Descrição: {tarefa['Descrição']}")

    elif opcao == 3:
        try:
            numero = int(input("Digite o númeo da tarefa para remover:"))
            if 0 <= numero <len(tarefas):
                tarefas.pop(numero)
                print("Tarefa removida!")
            else:
                print("Número inválido")
        except ValueError:
            print("Digite apenas números.")   

    else:
        print("Opção inválida, tente novamente.") 

    
        

        

    