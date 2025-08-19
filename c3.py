# crie uma classe chamada animal
# animal terá 3 atributos
# nome, peso idade

# crie 3 objeto para a classe animal
# girafa, gato, leão

# crie o método comer onde este método informará 
# que o animal que chamou o método está comendo.


class Animal:
    def __init__ (self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        
    def comer(self):
        print(f'{self.nome} está comendo!')
    
    
    def imc(self, peso, altura):
        imc = peso / (altura * altura)
        print(f'{self.nome} tem o {imc}')
    
        
a1 = Animal("girafa", 80, 3.85)
a2 = Animal('Gato', 2, 0.8)
a3 = Animal("Leão", 80, 1.30)


a1.comer()
a2.comer()
a3.comer()
        
a1.imc()
a2.imc()
a3.imc()