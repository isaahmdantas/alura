from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'Bebida: {self._nome}, Preço: R$: {self._preco:.2f}, Tamanho: {self._tamanho}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08) # Aplicanto um desconto de 5%