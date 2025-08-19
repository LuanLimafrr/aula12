class Carro:
    def ___init___(self, nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
        
fusca = Carro('fusca')
print('Nome : ',fusca.nome)
fusca.acelerar()

byd = Carro('BTD')
print('Nome: ',byd.nome)    
byd.acelerar()
