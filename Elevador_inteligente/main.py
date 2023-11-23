class Elevador:
    def __init__(self):
        self.totalCapacidade = 10
        self.atualCapacidade = 0
        self.totalAndar = 20
        self.atualAndar = 0

    def subir(self, andar):
        if self.atualAndar + andar <= self.totalAndar:
            self.atualAndar += andar
            print('Subindo!')
        else:
            andar_disponivel = self.totalAndar - self.atualAndar
            if self.atualAndar + andar == self.totalAndar:
                print("Você está no andar mais alto!")
            elif self.atualAndar == self.totalAndar - 1:
                print(f'O elevador sobe no máximo mais 1 andar.')
            else:
                print(f'O elevador sobe no máximo mais {andar_disponivel} andares.')
        print('\n')
        print(35 * '#')
        print('\n')  

    def descer(self, andar):
        if self.atualAndar - andar >= 0:
            self.atualAndar -= andar
            print('Descendo!')
        else:
            if self.atualAndar == 0:
                print("Você está no térreo!")
            elif self.atualAndar == 1:
                print(f'O elevador desce no máximo mais 1 andar.')
            else:
                print(f'O elevador desce no máximo mais {self.atualAndar} andares.')
        print('\n')
        print(35 * '#')
        print('\n')  

    def entrar(self, pessoa):
        if self.atualCapacidade + pessoa <= self.totalCapacidade:
            self.atualCapacidade += pessoa
            if pessoa > 1:
                print(f'Entrando {pessoa} pessoas.')
            else:
                print('Entrando 1 pessoa.')
        else:
            disponivel = self.totalCapacidade - self.atualCapacidade
            if self.atualCapacidade == self.totalCapacidade:
                print('O elevador está cheio!')
            elif disponivel == self.totalCapacidade - 1:
                print(f'O elevador só possui mais {disponivel} vaga.')
            else:
                print(f'O elevador só possui mais {disponivel} vagas.')
        print('\n')
        print(35 * '#')
        print('\n')  

    def sair(self, pessoa):
        if self.atualCapacidade - pessoa >= 0:
            self.atualCapacidade -= pessoa
            if pessoa > 1:
                print(f'Saindo {pessoa} pessoas.')
            else:
                print('Saindo 1 pessoa.')
        else:
            if self.atualCapacidade == 0:
                print('O elevador está vazio!')
            elif self.atualCapacidade == 1:
                print(f'O elevador só possui mais 1 pessoa.')
            else:
                print(f'O elevador só possui {self.atualCapacidade} pessoas.')
        print('\n')
        print(35 * '#')
        print('\n')  

elevador = Elevador()

while True:
    escolha = int(input('Escolha uma opção:\n'
                        '1 - Entrar\n'
                        '2 - Sair\n'
                        '3 - Subir\n'
                        '4 - Descer\n'
                        '0 - Encerrar programa\n'))

    match escolha:
        case 1:
            pessoa = int(input('Quantas pessoas vão entrar?\n'))
            elevador.entrar(pessoa)
        case 2:
            pessoa = int(input('Quantas pessoas vão sair?\n'))
            elevador.sair(pessoa)
        case 3:
            andar = int(input('Quantos andares você deseja subir?\n'))
            elevador.subir(andar)
        case 4:
            andar = int(input('Quantos andares você deseja descer?\n'))
            elevador.descer(andar)
        case 0:
            break
        case _:
            print('Você digitou uma opção inválida!')
