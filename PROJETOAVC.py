class SistemaLoja:
    def __init__(self):
        # Lista de produtos armazenados como dicionário
        self.estoque = {
            "Smartphone": {"categoria": "Eletrônicos", "preco": 1500.00, "quantidade": 10},
            "Camiseta": {"categoria": "Vestuário", "preco": 50.00, "quantidade": 20},
            "Notebook": {"categoria": "Eletrônicos", "preco": 3000.00, "quantidade": 5},
            "Calça": {"categoria": "Vestuário", "preco": 120.00, "quantidade": 15},
        }
        self.pedidos = {}


    def adicionar_produto(self, nome, categoria, preco, quantidade):
        self.estoque[nome] = {"categoria": categoria, "preco": preco, "quantidade": quantidade}

    def checar_estoque(self, nome_produto, quantidade):
        return nome_produto in self.estoque and self.estoque[nome_produto]["quantidade"] >= quantidade

    def atualizar_estoque(self, nome_produto, quantidade):
        if nome_produto in self.estoque:
            self.estoque[nome_produto]["quantidade"] -= quantidade

    def adicionar_pedido(self, cliente, nome_produto, quantidade):
        if cliente not in self.pedidos:
            self.pedidos[cliente] = {}
        if self.checar_estoque(nome_produto, quantidade):
            if nome_produto in self.pedidos[cliente]:
                self.pedidos[cliente][nome_produto] += quantidade
            else:
                self.pedidos[cliente][nome_produto] = quantidade
            print(f"{quantidade} unidade(s) de {nome_produto} adicionada(s) ao pedido de {cliente}.")
        else:
            print(f"Estoque insuficiente para {nome_produto}.")

    def remover_pedido(self, cliente, nome_produto):
        if cliente in self.pedidos and nome_produto in self.pedidos[cliente]:
            del self.pedidos[cliente][nome_produto]
            print(f"{nome_produto} removido do pedido de {cliente}.")
        else:
            print(f"{nome_produto} não está no pedido de {cliente}.")

    def calcular_total(self, cliente):
        total = 0
        if cliente in self.pedidos:
            for produto, quantidade in self.pedidos[cliente].items():
                total += self.estoque[produto]["preco"] * quantidade
        return total

    def aplicar_desconto(self, total):
        return total * 0.9 if total > 500 else total

    def concluir_compra(self, cliente):
        total = self.calcular_total(cliente)
        total_com_desconto = self.aplicar_desconto(total)

        print(f"Total da compra de {cliente}: R$ {total:.2f}")
        print(f"Total com desconto: R$ {total_com_desconto:.2f}")
        for produto, quantidade in self.pedidos[cliente].items():
            self.atualizar_estoque(produto, quantidade)

        del self.pedidos[cliente]
        print(f"Compra finalizada para {cliente}. Pedido cancelado.")

    def listar_produtos(self):
        print("Produtos disponíveis na loja:")
        for nome, info in self.estoque.items():
            print(f"Nome: {nome}, Categoria: {info['categoria']}, Preço: R$ {info['preco']:.2f}, Estoque: {info['quantidade']}")
# Demonstração de uso do sistema
loja_virtual = SistemaLoja()
loja_virtual.listar_produtos()
# Cliente adiciona produtos ao pedido
loja_virtual.adicionar_pedido("Ana", "Smartphone", 1)
loja_virtual.adicionar_pedido("Ana", "Camiseta", 3)
# Cliente remove um produto
loja_virtual.remover_pedido("Ana", "Camiseta")
# Finaliza a compra
loja_virtual.concluir_compra("Ana")
# Lista produtos após a compra
loja_virtual.listar_produtos()

