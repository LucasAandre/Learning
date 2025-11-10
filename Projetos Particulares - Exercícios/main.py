'''
Você foi contratado para desenvolver um sistema de gerenciamento de funcionários de uma empresa.
A empresa possui funcionários comuns e gerentes, mas pretende futuramente adicionar outros tipos (como estagiários, diretores, etc.).
Para isso, o sistema deve ser flexível e usar herança, polimorfismo e classes abstratas.

Instruções:

1. Crie uma classe abstrata chamada Funcionario:

    - Deve conter os atributos:

        nome (string)

        salario_base (float)

    - Deve ter:

        Um método abstrato chamado calcular_bonus(), que retornará o bônus do funcionário.

        Um método concreto mostrar_informacoes() que exibe o nome e o salário base.

2. Crie uma classe FuncionarioComum que herda de Funcionario:

    - O bônus é 10% do salário base.

    - Deve sobrescrever o método calcular_bonus().

3. Crie uma classe Gerente, também herdeira de Funcionario:

    - O bônus é 25% do salário base + R$ 1.000 de adicional fixo.

    - Deve sobrescrever o método calcular_bonus().

4. Demonstre o polimorfismo:

    - Crie uma lista com objetos de FuncionarioComum e Gerente.

    - Faça um loop que percorre a lista e chame o método calcular_bonus() para cada um, mostrando os resultados.
'''
from modelos.funcionario import Funcionario
from modelos.funcionario_comum import FuncionarioComum
from modelos.gerente import Gerente

def main():
    print('''
            █▀▀ █▀█ █▄░█ ▀█▀ █▀█ █▀█ █░░ █▀▀   █▀▄ █▀▀   █▀▀ █░█ █▄░█ █▀▀ █ █▀█ █▄░█ ▄▀█ █▀█ █ █▀█ █▀
            █▄▄ █▄█ █░▀█ ░█░ █▀▄ █▄█ █▄▄ ██▄   █▄▀ ██▄   █▀░ █▄█ █░▀█ █▄▄ █ █▄█ █░▀█ █▀█ █▀▄ █ █▄█ ▄█
          ''')
    print()

    while True:
        nome = input('\nDigite o nome do funcionário: ').title()
        salario = float(input('Digite o salário base do funcionário: '))
        cargo = input('Digite o cargo do funcionário: ')

        if cargo.lower() == 'gerente':
            funcionario = Gerente(nome, salario, cargo)

        else:
            funcionario = FuncionarioComum(nome, salario, cargo)

        funcionario.calcular_bonus()

        escolha = input('Deseja cadastrar mais um funcionário? [SIM / NÃO]: ').upper()
        print()

        if 'N' in escolha:
            break

    Funcionario.listar_funcionarios()

if __name__ == '__main__':
    main()
