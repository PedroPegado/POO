class Carro:
    def __init__(self, marca, marcha, cor):
        self.marca = marca
        self.marcha = marcha
        self.cor = cor

    def ligar(self):
        print('LIGANDO... VRUM VRUM')
    
    def desligar(self):
        print('UuUeUmmmm, DESLIGANDO...')

    def manual_do_carro(self):
        print(self.marca, self.marcha, self.cor)



marca = input('Qual o seu carro? ')
marcha = input('Qual a marcha? ')
cor = input('Qual a cor? ')

carro1 = Carro(marca, marcha, cor)
carro1.ligar()
carro1.desligar()
carro1.manual_do_carro()
