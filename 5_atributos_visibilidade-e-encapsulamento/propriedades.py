class Quadrado:
    def __init__(self, medida):
        self.altura = medida
        self.largura = medida

    @property   # property - declaração de uma propriedade
    def altura(self):
        print('getter de altura')
        return self.__medida

# sem o setter, a propriedade fica "encapsulada"
    @altura.setter   # setter - método que altera uma propriedade
    def altura(self, valor):
        print('setter de altura')
        if valor < 0:
            raise ValueError()
        self.__medida = valor


    @property
    def largura(self):
        print('getter de largura')
        return self.__medida

    @largura.setter
    def largura(self, valor):
        print('setter de largura')
        if valor < 0:
            raise ValueError()
        self.__medida = valor

    def area(self):
        return self.largura * self.altura

quadrado = Quadrado(2)
quadrado.altura = 3
print(quadrado.area())