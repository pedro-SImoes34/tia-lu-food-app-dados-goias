menu_de_itens = []
proximo_codigo = 1

def cadastrar_item():
    global proximo_codigo
    print("\n--- Cadastrar Novo Item ---")
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição: ")
    preco = float(input("Digite o preço: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    novo_item = ([proximo_codigo, nome, descricao, preco, estoque])
    menu_de_itens.append(novo_item)
    proximo_codigo += 1
    print("Item cadastrado com sucesso!")


def atualizar_item():
    codigo = int(input("\n Digite o código do item a ser atualizado:  "))
    for item in menu_de_itens:
        if item[0] == codigo:
            print(f"\nEditando item {item[1]} (código {0})")
            novo_nome = input(f"Novo nome ({item[1]}): ")
            if novo_nome:
                 item[1] = novo_nome
            nova_desc= input(f"Nova descrição ({item[2]}): ")
            if nova_desc:
                 item[2] = nova_desc
            novo_preco= input(f"Novo preço ({item[3]}): ")
            if novo_preco:
                item[3] = float(novo_preco)
            novo_estoque = input(f"Novo estoque ({item[4]}): ")
            if novo_estoque:
                item[4] = int(novo_estoque)
            print("\n✅ Item atualizado com sucesso!\n")
            return
    print("\n❌ Item não encontrado!\n")

def consultar_itens():
    if not menu_de_itens:
        print("\n⚠ Nenhum item cadastrado.\n")
        return
    print("\n📋 Lista de Itens:")
    for item in menu_de_itens:
        print(f"[{item[0]}] {item[1]} - R${item[3]:.2f} (Estoque: {item[4]})")
    print()
        
def detalhes_item():
    codigo = int(input("\n Digite o código do item:  "))
    for item in menu_de_itens:
        if item[0] == codigo:
            print("\n🔎 Detalhes do Item:")
            print(f"Código: {item[0]}")
            print(f"Nome: {item[1]}")
            print(f"Descrição: {item[2]}")
            print(f"Preço: R${item[3]:.2f}")
            print(f"Estoque: {item[4]}\n")
            return
    print("\n❌ Item não encontrado!\n")

def menu_principal():
    menu = 0
    while menu == 0:
        print("\n === MENU PRINCIPAL ===")
        print("1 - Cadastrar Item")
        print("2 - Atualizar Item")
        print("3 - Consultar Itens")
        print("4 - Detalhes do Item")
        print("0 - Sair")

        opcao = input("\n Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_item()
        elif opcao == "2":
            atualizar_item()
        elif opcao == "3":
            consultar_itens()
        elif opcao == "4":
            detalhes_item()
        elif opcao == "0":
            print("\n👋 Saindo do sistema. Até mais!")
            break
        else:
            print("\n⚠ Opção inválida, tente novamente.\n")

menu_principal()
           
fila_pedidos_pendentes = []  
fila_pedidos_aceitos = []    
fila_pedidos_prontos = []     
fila_pedidos_entrega = []     
todos_pedidos = []
valor_total = 0

def criar_pedido(nome_cliente, itens):
    codigo = len(todos_pedidos) + 1 
    valor_total = 0
    
    for item in menu_de_itens:
        if item[0] == itens: #verifica se o código do produto está na lista de itens escolhidos
            valor_total += item[3]

    valido = 0
    while valido == 0: 
        desconto = input("Deseja adicionar algum cupom de desconto? (S/N): ")
        cupom = "GOIAS10"
        
        if desconto == "S":
            cupom = input("Digite o cupom: ") 
            if cupom == "GOIAS10":
                valor_desconto = valor_total * 0.1 
                valor_total -= valor_desconto
                print("\n Você ganhou 10% de desconto!")
                print(f"O valor do seu pedido acabou de cair para R${valor_total:.2f}!!")
                valido = 1     
            else:
                print("Cupom inválido!")
                print("1 - Tentar novamente.")
                print("2 - Continuar sem cupom.")
                resposta = int(input("Escolha uma opção: "))
                
                if resposta == 1:
                    valido = 0              
                elif resposta == 2:
                    print(f"O seu pedido ficou no valor de R${valor_total:.2f}")
                    valido = 1
                else:
                    print("Não consegui te entender, tente inserir o cupom novamente...")
                    valido = 0
        elif desconto == "N":
            print(f"O seu pedido ficou no valor de R${valor_total:.2f}")
            valido = 1
        else:
            print("Desculpe, não entendi sua resposta, tente novamente.")
        
    pedido = [codigo, nome_cliente, itens, "AGUARDANDO APROVACAO", valor_total]     
    fila_pedidos_pendentes.append(pedido)  # vai para a fila de pendentes
    todos_pedidos.append(pedido)           # também entra no histórico
    print(f"Pedido {codigo} criado para {nome_cliente} e está AGUARDANDO APROVACAO.")


def processar_pedido():
    if len(fila_pedidos_pendentes) == 0:
        print("Nenhum pedido pendente para processar.")
    else:
        pedido = fila_pedidos_pendentes.pop(0)  # pega o mais antigo
        print(f"Processando pedido {pedido[0]} de valor R${pedido[4]:.2f} do cliente {pedido[1]}")
        print("1 - Aceitar pedido")
        print("2 - Rejeitar pedido")
        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            pedido[3] = "ACEITO"
            fila_pedidos_aceitos.append(pedido)
            print(f"Pedido {pedido[0]} foi ACEITO e está na fila de preparo.")
        else:
            pedido[3] = "REJEITADO"
            print(f"Pedido {pedido[0]} foi REJEITADO.")

def preparar_pedido():
    if len(fila_pedidos_aceitos) == 0:
        print("Nenhum pedido aceito para preparar.")

    else:
        pedido = fila_pedidos_aceitos.pop(0)
        print(f"\n Deseja prosseguir com o pedido {pedido[0]} de {pedido[1]} no valor de {pedido[4]}?")
        print("1- Prosseguir com o pedido")  
        print("2- Cancelar o pedido")
        escolha = input("Digite a sua escolha: ")

        if escolha == "1":
            pedido[3] = "FAZENDO"
            print(f"Pedido {pedido[0]} está sendo preparado...")
            pedido[3] = "FEITO"
            fila_pedidos_prontos.append(pedido)
            print(f"Pedido {pedido[0]} está FEITO e agora ESPERANDO ENTREGADOR.")
        
        elif escolha == "2":
            pedido[3] = "CANCELADO"
            print(f"Pedido {pedido[0]} foi cancelado.")


def enviar_para_entrega():
    if len(fila_pedidos_prontos) == 0:
        print("Nenhum pedido pronto para enviar.")
    else:
        pedido = fila_pedidos_prontos.pop(0)
        pedido[3] = "SAIU PARA ENTREGA"
        fila_pedidos_entrega.append(pedido)
        print(f"Pedido {pedido[0]} de {pedido[1]} SAIU PARA ENTREGA.")


def finalizar_entrega():
    if len(fila_pedidos_entrega) == 0:
        print("Nenhum pedido em rota de entrega.")
    else:
        pedido = fila_pedidos_entrega.pop(0)
        pedido[3] = "ENTREGUE"
        print(f"Pedido {pedido[0]} foi ENTREGUE ao cliente {pedido[1]}.")


def exibir_pedidos():
    print("\n--- LISTA DE PEDIDOS ---")
    for pedido in todos_pedidos:
        print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Status: {pedido[3]}")
    print("-------------------------\n")

def filtrar_pedidos():
    print("----- TODOS OS STATUS -----")
    print("1 - AGUARDANDO APROVACAO")
    print("2 - ACEITO")
    print("3 - FAZENDO")
    print("4 - FEITO")
    print("5 - ESPERANDO ENTREGADOR")
    print("6 - SAIU PARA ENTREGA")
    print("7 - ENTREGUE")
    print("8 - CANCELADO")
    print("9 - REJEITADO")
    filtro = input("Qual status deseja usar como filtro: ")
    if filtro == "1":
        for pedido in todos_pedidos:
            if pedido[3] == "AGUARDANDO APROVACAO":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe mais pedidos com esse status no momento.")
    
    if filtro == "2":
        for pedido in todos_pedidos:
            if pedido[3] == "ACEITO":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe pedidos com esse status no momento.")

    if filtro == "3":
        for pedido in todos_pedidos:
            if pedido[3] == "FAZENDO":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe pedidos com esse status no momento.")

    if filtro == "4":
        for pedido in todos_pedidos:
            if pedido[3] == "FEITO":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe pedidos com esse status no momento.")

    if filtro == "5":
        for pedido in todos_pedidos:
            if pedido[3] == "ESPERANDO ENTREGADOR":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe pedidos com esse status no momento.")

    if filtro == "6":
        for pedido in todos_pedidos:
            if pedido[3] == "SAIU PARA ENTREGA":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe pedidos com esse status no momento.")

    if filtro == "7":
        for pedido in todos_pedidos:
            if pedido[3] == "ENTREGUE":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe pedidos com esse status no momento.")

    if filtro == "8":
        for pedido in todos_pedidos:
            if pedido[3] == "CANCELADO":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe pedidos com esse status no momento.")

    if filtro == "9":
        for pedido in todos_pedidos:
            if pedido[3] == "REJEITADO":
                print(f"Código: {pedido[0]} | Cliente: {pedido[1]} | Itens: {pedido[2]} | Status: {pedido[3]} | Valor do Pedido: {pedido[4]:.2f}")
            else:
                print("Não existe pedidos com esse status no momento.")





def menu_pedidos():
    sair = 0
    while sair == 0:
        print("\n ------ SISTEMA DE PEDIDOS ------")
        print("1 - Criar Pedido")
        print("2 - Processar Pedido Pendente")
        print("3 - Preparar Pedido")
        print("4 - Enviar para Entrega")
        print("5 - Finalizar Entrega")
        print("6 - Exibir todos os pedidos")
        print("7 - Filtrar pedidos por status")
        print("8 - Voltar ao menu anterior")
        print("9 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("\n Nome do cliente: ")
            itens = int(input("Itens do pedido: "))

            item_encontrado = False
            for novo_item in menu_de_itens:
                if itens == novo_item[0]:
                    item_encontrado = True
                    if novo_item[4] > 0:
                        criar_pedido(nome, itens)
                        novo_item[4] -= 1
                    else:
                        print("No momento estamos em falta deste item. Sentimos muito por isso ☹️")
                    break
            if not item_encontrado:
                print("Item não encontrado, tente novamente.")

        elif opcao == "2":
            processar_pedido()
        elif opcao == "3":
            preparar_pedido()
        elif opcao == "4":
            enviar_para_entrega()
        elif opcao == "5":
            finalizar_entrega()
        elif opcao == "6":
            exibir_pedidos()
        elif opcao == "7":
            filtrar_pedidos()
        elif opcao == "8":
            menu_principal()
        elif opcao == "9":
            sair = 1
            print("Saindo do sistema...")
        else:
            print("Opção inválida, tente de novo.")

menu_pedidos()