from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): # Declarando que a classe Prato é "filho" da classe ItemCardapio --> HERANÇA
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) # super() é um objeto especial que permite que infos de outra classe (classe pai) sejam acessados
        self.descricao = descricao
    
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
    