# Estoque formado por lista
stock = []

while True:
    print(20 * "-", "Controle de Estoque", 20 * "-")
    print("Selecione uma das opções abaixo")
    print("1 - Visualizar estoque")
    print("2 - Adicionar novo produto")
    print("3 - Remover produto do estoque")
    print("4 - Atualizar preço de um produto")
    print("5 - Atualizar quantidade de um produto")
    print("6 - Sair")

    try:
        choice = int(input("> "))
    except ValueError:
        print("Operação inválida, tente novamente")
        continue

    if choice == 1:
        print(20 * "-", "Estoque Atual", 20 * "-")
        if not stock:
            print("Estoque vazio.")
        else:
            for product in stock:
                print(f"Nome: {product['nome']}")
                print(f"Valor: R$ {product['valor']:.2f}")
                print(f"Quantidade: {product['quantidade']}")
                print(50 * "-")
    elif choice == 2:
        nome = input("Informe Nome do Produto: ")
        try:
            valor = float(input("Informe o valor do Produto: "))
            quantidade = int(input("Informe a quantidade do produto: "))
        except ValueError:
            print("Valores inválidos. Tente novamente.")
            continue
        new_product = {"nome": nome, "valor": valor, "quantidade": quantidade}
        stock.append(new_product)
        print(f"Produto {nome} adicionado com sucesso!")
    elif choice == 3:
        nome = input("Informe o nome do produto a ser removido: ")
        for product in stock:
            if product['nome'].lower() == nome.lower():
                stock.remove(product)
                print(f"Produto {nome} removido com sucesso!")
                break
        else:
            print(f"Produto {nome} não encontrado.")
    elif choice == 4:
        nome = input("Informe o nome do produto para atualizar o preço: ")
        for product in stock:
            if product['nome'].lower() == nome.lower():
                try:
                    novo_valor = float(input(f"Informe o novo valor para {product['nome']}: "))
                except ValueError:
                    print("Valor inválido. Tente novamente.")
                    break
                product['valor'] = novo_valor
                print(f"Preço do produto {product['nome']} atualizado para R$ {novo_valor:.2f}")
                break
        else:
            print(f"Produto {nome} não encontrado.")
    elif choice == 5:
        nome = input("Informe o nome do produto para atualizar a quantidade: ")
        for product in stock:
            if product['nome'].lower() == nome.lower():
                try:
                    nova_quantidade = int(input(f"Informe a nova quantidade para {product['nome']}: "))
                except ValueError:
                    print("Quantidade inválida. Tente novamente.")
                    break
                product['quantidade'] = nova_quantidade
                print(f"Quantidade do produto {product['nome']} atualizada para {nova_quantidade}")
                break
        else:
            print(f"Produto {nome} não encontrado.")
    elif choice == 6:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente")