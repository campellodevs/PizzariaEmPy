def forca_opcao(opcoes, msg):
    listar_opcoes = '\n'.join(opcoes)
    opcao = input(f"{msg}\n{listar_opcoes}\n -> ")
    while opcao not in opcoes:
        opcao = input(f"Escolha uma opção válida!\n{listar_opcoes}\n -> ")
    return opcao


def index(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i


def exibir_cardapio(pizzaria):
    print("Cardápio:")
    pizzas = pizzaria['pizzas']
    precos = pizzaria['preço']
    for i in range(len(pizzas)):
        print(f"{i + 1}. {pizzas[i]} - R${precos[i]}")


def isnumeric(msg, msg_erro='Inválido'):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)


def atualizar_carrinho(carrinho, pizza, quantidade, preco, endereco):
    if pizza in carrinho['Pizzas']:
        carrinho['Pizzas'][pizza]['quantidade'] += quantidade
        carrinho['Pizzas'][pizza]['preço'] += preco
    else:
        carrinho['Pizzas'][pizza] = {'quantidade': quantidade, 'preço': preco}
    carrinho['Valor total'] += preco
    carrinho['Endereço'] = endereco


pizzaria = {
    'pizzas': ['Calabresa', '4 Queijos', 'Strogonoff', 'Peperoni', 'Frango com Catupiry'],
    'peso(g)': [1200, 800, 740, 1500, 1000],
    'preço': [50, 70, 100, 30, 40],
    'estoque': [4, 17, 21, 2, 5],
    'nacionalidade': ['Brasil', 'Itália', 'Rússia', 'USA', 'Argentina']
}

dic_indices = {pizzaria['pizzas'][i]: i for i in range(len(pizzaria['pizzas']))}

print("Seja bem-vindo à pizzaria do Campello!")

tipo_usuario = forca_opcao(['Funcionário', 'Cliente'], "Em qual você se encaixa")

while True:
    exibir_cardapio(pizzaria)

    carrinho = {
        'Pizzas': {},
        'Valor total': 0,
        'Endereço': {
            'Rua': '',
            'Número': '',
            'CEP': '',
            'Complemento': '',
            'Cidade': '',
            'Estado': '',
        },
    }

    valor_total = 0

    while True:
        opcaopizza = forca_opcao(pizzaria['pizzas'], "Escolha uma das opções:")
        indice_pizza = index(pizzaria['pizzas'], opcaopizza)
        indice_escolha = dic_indices[opcaopizza]
        preço_pizza = pizzaria['preço'][indice_pizza]

        qtd = isnumeric(f"Quantas Pizzas de {opcaopizza} você quer? \n -> ")

        if qtd > pizzaria['estoque'][indice_escolha]:
            print("Desculpe, não há estoque suficiente.")
            continue

        valor_total += qtd * preço_pizza
        pizzaria['estoque'][indice_escolha] -= qtd
        print(
            f"A pizza escolhida é a {opcaopizza}, a {indice_pizza + 1}ª opção do cardápio! O preço é R${preço_pizza}.")
        print(f"Valor total a pagar: R${valor_total}.")

        if carrinho['Endereço']['Rua'] == '':
            for campo in carrinho['Endereço']:
                carrinho['Endereço'][campo] = input(f"Digite o {campo} de entrega: ")

        atualizar_carrinho(carrinho, opcaopizza, qtd, preço_pizza, carrinho['Endereço'])
        print(f"Carrinho Atualizado {carrinho}")

        continuar = forca_opcao(['sim', 'não'], "Deseja comprar mais alguma coisa? (sim/não)")
        if continuar == 'não':
            break

    print(f"Total da compra: R${valor_total}. Sua pizza chegará em aproximadamente 40 minutos.")

    nova_compra = forca_opcao(['sim', 'não'], "Deseja fazer uma nova compra? (sim/não)")
    if nova_compra == 'não':
        print("Obrigado por comprar conosco! Até a próxima!")
        break
