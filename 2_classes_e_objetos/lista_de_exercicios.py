# 1. Crie uma classe que modele o objeto "carro".   
# 2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# 4. Crie uma instância da classe carro.
# 5. Faça o carro "andar" utilizando os métodos da sua classe.
# 6. Faça o carro "parar" utilizando os métodos da sua classe.


class carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'branco'
        self.modelo = 'Fusca'
        self.velocidade = 0

    def liga(self):
        self.ligado = True
    
    def desliga(self):
        self.ligado = False
    
    def acelera(self):
        if self.ligado:
            self.velocidade += 10
        if self.velocidade > 200:
            self.velocidade = 200
    print('Velocidade máxima atingida.')

    def desacelera(self):
        if self.ligado:
            self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0
    print('Velocidade mínima atingida.')

    def __str__(self):
        return f'Carro - ligado: {self.ligado}, cor: {self.cor}, modelo: {self.modelo}, velocidade: {self.velocidade}'
    
    
carro_teste = carro()

carro_teste.liga()

print(carro_teste)

carro_teste.acelera()

print(carro_teste)

carro_teste.acelera()

print(carro_teste)

carro_teste.desacelera()

print(carro_teste)

carro_teste.desliga()

print(carro_teste)







