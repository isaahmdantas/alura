from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida 
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_morango = Sobremesa('Mousse de Morango', 10.00, 'Deliciosa mousse de morango', 'Doce', 'Pequeno')
sobremesa_morango.aplicar_desconto()

restaurante_praca.adicionar_item_no_cardapio(bebida_suco)
restaurante_praca.adicionar_item_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_item_no_cardapio(sobremesa_morango)

def main():
    Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()