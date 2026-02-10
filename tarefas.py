tarefas = []

def mostrar():
    print("OPÇÔES")
    print("1 - Adicionar Tarefas")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefas")
    print("4 - Editar Tarefa")
    print("5 - Marcar/Desmarcar Tarefa concluída")
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
        try:
            registro = int(input("Digite quantas tarefas deseja registrar: "))
            for r in range(registro):
                titulo = input("Digite o título da Tarefa: ")
                descricao = input("Digite a descrição da tarefa: ")

                tarefa = {
                    "Titulo":titulo,
                    "Descrição":descricao,
                    "concluida": False
                }

                tarefas.append(tarefa)
                print("Tarefa adicionada!")
        except ValueError:
            print("Digite apenas números.")

    elif opcao == 2:
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(tarefas):
                status = "✅" if tarefa["concluida"] else "❌"
                print(f"{i + 1} - {tarefa['Titulo']} [{status}]")
                print(f" Descrição: {tarefa['Descrição']}")

    elif opcao == 3:
        try:
            numero = int(input("Digite o númeo da tarefa para remover:")) - 1
            if 0 <= numero <len(tarefas):
                tarefas.pop(numero)
                print("Tarefa removida!")
            else:
                print("Número inválido")
        except ValueError:
            print("Digite apenas números.")   
        
    elif opcao == 4:
        if not tarefas:
            print("Nenhuma tarefa para editar.")
            continue
        try:
            numero = int(input("Digite o número da tarefa que deseja editar: ")) - 1
            if 0 <= numero <len(tarefas):
                tarefa = tarefas[numero]
                print(f"Título atual: {tarefa['Titulo']}")
                novo_titulo = input("Digite o novo título (ou ENTER para desistir): ")
                if novo_titulo.strip():  #caso não tenha apertado o enter
                    tarefa['Titulo'] = novo_titulo

                print(f"Descrição atual: {tarefa['Descrição']}")
                nova_descricao = input("Digite a nova descrição (ou ENTER para desistir)")
                if nova_descricao.strip():
                    tarefa['Descrição'] = nova_descricao
                print("Tarefa atualizada!")

            else:
                print("Número inválido")
        except ValueError:
            print("Digite apenas números.")

    elif opcao == 5:
        if not tarefas:
            print("Nenhuma tarefa para marcar.")
            continue
        try:
            numero = int(input("Digite o número da tarefa para marcar/desmarcar: ")) - 1
            if 0 <= numero < len(tarefas):
                tarefa = tarefas[numero]
                tarefa["concluida"] =  not tarefa["concluida"]
                simbolo = "✅ " if tarefa["concluida"] else "❌"
                print(f"Tarefa '{tarefa['Titulo']}' agora está {simbolo}.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite apenas números.")
    else:
        print("Opção inválida, tente novamente.") 

    
        

        

    