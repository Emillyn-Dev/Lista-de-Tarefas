# Cria uma lista vazia para armazenar todas as tarefas
tarefas = []

# Função para mostrar o menu de opções do usuário
def mostrar():
    print("OPÇÔES")
    print("1 - Adicionar Tarefas")             # Opção para adicionar novas tarefas
    print("2 - Listar Tarefas")               # Opção para exibir todas as tarefas
    print("3 - Remover Tarefas")              # Opção para remover uma tarefa existente
    print("4 - Editar Tarefa")                # Opção para editar título ou descrição de uma tarefa
    print("5 - Marcar/Desmarcar Tarefa concluída")  # Opção para alternar entre ✅ e ❌
    print("0 - Sair")                         # Opção para encerrar o programa

# Loop principal do programa, executa até que o usuário escolha sair
while True:
    mostrar()  # Mostra o menu de opções
    
    try:
        # Solicita a opção do usuário e converte para inteiro
        opcao = int(input("Digite sua opção: "))
        
    except ValueError:
        # Caso o usuário digite algo que não seja número
        print("Por favor, utilize apenas números válidos")
        continue  # Volta para o início do loop

    # Se o usuário escolher 0, sai do programa
    if opcao == 0:
        print("Saindo do Programa...")
        break  # Encerra o loop principal

    # Adicionar tarefas
    elif opcao == 1:
        try:
            # Pergunta quantas tarefas o usuário quer adicionar
            registro = int(input("Digite quantas tarefas deseja registrar: "))
            
            # Loop para adicionar múltiplas tarefas
            for r in range(registro):
                titulo = input("Digite o título da Tarefa: ")        # Solicita o título
                descricao = input("Digite a descrição da tarefa: ")  # Solicita a descrição

                # Cria um dicionário com os dados da tarefa
                tarefa = {
                    "Titulo": titulo,
                    "Descrição": descricao,
                    "concluida": False  # Inicializa como pendente (❌)
                }

                # Adiciona a tarefa à lista
                tarefas.append(tarefa)
                print("Tarefa adicionada!")  # Confirmação para o usuário
        except ValueError:
            # Caso o usuário digite algo que não seja número
            print("Digite apenas números.")

    # Listar tarefas
    elif opcao == 2:
        if not tarefas:
            # Caso a lista esteja vazia
            print("Nenhuma tarefa na lista.")
        else:
            # Percorre todas as tarefas da lista
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(tarefas):
                # Define o símbolo ✅ ou ❌ dependendo do status
                status = "✅" if tarefa["concluida"] else "❌"
                # Mostra o número, título e status da tarefa
                print(f"{i + 1} - {tarefa['Titulo']} [{status}]")
                # Mostra a descrição da tarefa
                print(f" Descrição: {tarefa['Descrição']}")

    # Remover tarefas
    elif opcao == 3:
        try:
            # Solicita o número da tarefa que o usuário quer remover
            numero = int(input("Digite o númeo da tarefa para remover:")) - 1
            if 0 <= numero < len(tarefas):
                # Remove a tarefa da lista usando pop
                tarefas.pop(numero)
                print("Tarefa removida!")
            else:
                # Caso o número esteja fora do intervalo da lista
                print("Número inválido")
        except ValueError:
            # Caso o usuário digite algo que não seja número
            print("Digite apenas números.")   

    # Editar tarefas
    elif opcao == 4:
        if not tarefas:
            print("Nenhuma tarefa para editar.")
            continue  # Volta para o início do loop
        
        try:
            # Solicita o número da tarefa que deseja editar
            numero = int(input("Digite o número da tarefa que deseja editar: ")) - 1
            if 0 <= numero < len(tarefas):
                tarefa = tarefas[numero]  # Seleciona a tarefa
                
                # Editar título
                print(f"Título atual: {tarefa['Titulo']}")
                novo_titulo = input("Digite o novo título (ou ENTER para desistir): ")
                if novo_titulo.strip():  # Se o usuário digitou algo, atualiza o título
                    tarefa['Titulo'] = novo_titulo

                # Editar descrição
                print(f"Descrição atual: {tarefa['Descrição']}")
                nova_descricao = input("Digite a nova descrição (ou ENTER para desistir): ")
                if nova_descricao.strip():  # Se o usuário digitou algo, atualiza a descrição
                    tarefa['Descrição'] = nova_descricao
                
                print("Tarefa atualizada!")  # Confirmação
            else:
                print("Número inválido")
        except ValueError:
            print("Digite apenas números.")

    # Marcar ou desmarcar tarefa concluída
    elif opcao == 5:
        if not tarefas:
            print("Nenhuma tarefa para marcar.")
            continue
        
        try:
            # Solicita o número da tarefa
            numero = int(input("Digite o número da tarefa para marcar/desmarcar: ")) - 1
            if 0 <= numero < len(tarefas):
                tarefa = tarefas[numero]
                
                # Alterna o status da tarefa (True <-> False)
                tarefa["concluida"] = not tarefa["concluida"]
                
                # Define o símbolo correspondente
                simbolo = "✅" if tarefa["concluida"] else "❌"
                
                # Mostra mensagem com o status atualizado
                print(f"Tarefa '{tarefa['Titulo']}' agora está {simbolo}.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite apenas números.")

    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida, tente novamente.") 
