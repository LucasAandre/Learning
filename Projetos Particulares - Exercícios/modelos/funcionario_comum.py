from modelos.funcionario import Funcionario

class FuncionarioComum(Funcionario):
    def __init__(self, nome, salario_base, cargo):
        super().__init__(nome, salario_base, cargo)
    
    def __str__(self):
        return super().__str__()
    
    def calcular_bonus(self):
        self._bonus = float((self._salario_base * 0.1))
