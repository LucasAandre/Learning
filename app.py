from modelos.restaurante import Restaurante # Da pasta modelos e arquivo restaurante, importe a classe Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_hamburger = Restaurante("Deivid's Burger", 'Hamburger')
restaurante_mexicano = Restaurante('Sí Señor', 'Mexicana')
restaurante_arabe = Restaurante('Habybe', 'Árabe')

bebida_suco = Bebida('Suco de Abacaxi com Acerola', 5.00, 'Grande')
prato_fogazza = Prato('Fogazza de Calabresa', 10.00, 'A melhor fogazza da região')

restaurante_hamburger.adicionar_no_cardapio(bebida_suco)
restaurante_hamburger.adicionar_no_cardapio(prato_fogazza)

bebida_suco.aplicar_desconto()
prato_fogazza.aplicar_desconto()

def main():
    restaurante_hamburger.exibir_cardapio


if __name__ == '__main__': # Se for meu arquivo principal da aplicação (main)
    main()
