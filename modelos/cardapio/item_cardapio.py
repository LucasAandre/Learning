from abc import ABC, abstractmethod
'''
O módulo abc (de Abstract Base Classes) permite criar classes base abstratas, que servem como modelos para outras classes.
Elas definem métodos obrigatórios que as subclasses devem implementar.

ABC é uma classe especial usada como classe mãe.
Quando você herda de ABC, está dizendo que sua classe pode conter métodos abstratos.
'''

class ItemCardapio(ABC):
    def __init__(self, nome, preco): # Método Construtor
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass # Não precisa ter nada. Um método abstrato serve apenas para dizer às classes filhas: VOCÊS PRECISAM TER O MÉTODO aplicar_desconto()
    