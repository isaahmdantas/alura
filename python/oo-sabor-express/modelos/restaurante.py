from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato 
from modelos.cardapio.sobremesa import Sobremesa

class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_item_no_cardapio(self, item): 
        """ Adicionar um item ao cardápio do restaurante """
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self):
        """ Exibe o cardápio do restaurante """
        print(f'Cardápio do restaurante {self._nome}: ')
        for i, item in enumerate(self._cardapio, start=1):
            if isinstance(item, Prato):
                mensagem = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Descrição: {item._descricao}'
            elif isinstance(item, Bebida):
                mensagem = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Tamanho: {item._tamanho}'
            elif isinstance(item, Sobremesa):
                mensagem = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Tipo: {item._tipo} | Tamanho: {item._tamanho}  | Descrição: {item._descricao}'
            print(mensagem)
