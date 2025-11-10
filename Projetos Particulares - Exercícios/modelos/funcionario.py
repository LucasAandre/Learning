from abc import ABC, abstractmethod
import os

class Funcionario(ABC):
    funcionarios = []
    def __init__(self, nome, salario_base, cargo):
        self._nome = nome
        self._salario_base = float(salario_base)
        self._cargo = cargo
        self._bonus = 0
        Funcionario.funcionarios.append(self)
    
    def __str__(self):
        return f'Funcionário: {self._nome}'
    
    @abstractmethod
    def calcular_bonus(self):
        pass
    
    @property
    def mostrar_informacoes(self):
        return f'Nome: {self._nome} | Salário: R${self._salario_base} | Cargo: {self._cargo}'

    @classmethod
    def listar_funcionarios(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('==== LISTA DE FUNCIONÁRIOS ====\n')
        for f in cls.funcionarios:
            print(f'Nome: {f._nome}\nSalário: R${f._salario_base:.2f}\nCargo: {f._cargo}\nBônus: R${f._bonus:.2f}')
            print('-' * 25)
