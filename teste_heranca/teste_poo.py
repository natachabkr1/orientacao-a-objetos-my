# Exemplo de Herança em um Jogo de RPG Estilo Final Fantasy 

# Classe base  (é a abstração do objeto)
class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
        self.hp = 100 + (nivel * 10)
    
    def atacar(self):
        return f"{self.nome} ataca com uma arma básica."

    def receber_dano(self, dano):
        self.hp -= dano
        return f"{self.nome} recebeu {dano} de dano. HP restante: {self.hp}"

    def mostrar_status(self):
        return f"{self.nome} (Nível {self.nivel}): HP = {self.hp}"

# Subclasse para Guerreiro
class Guerreiro(Personagem):
    def __init__(self, nome, nivel):
        super().__init__(nome, nivel)  # "super" -> está chamando a classe mãe (super class)
        self.forca = 20 + (nivel * 5)
    
    def atacar(self):
        return f"{self.nome} ataca com uma espada poderosa! Dano: {self.forca}"

# # Subclasse para Mago
# class Mago(Personagem):
#     def __init__(self, nome, nivel):
#         super().__init__(nome, nivel)
#         self.mana = 50 + (nivel * 10)
    
#     def atacar(self):
#         return f"{self.nome} lança uma bola de fogo! Dano: {self.mana // 2}"

# # Subclasse para Arqueiro
# class Arqueiro(Personagem):
#     def __init__(self, nome, nivel):
#         super().__init__(nome, nivel)
#         self.precisao = 15 + (nivel * 4)
    
#     def atacar(self):
#         return f"{self.nome} dispara uma flecha precisa! Dano: {self.precisao}"

# Criando personagens
guerreiro = Guerreiro("Conan", 5)
guerreiro2 = Guerreiro("Chyrra", 6)

# guerreiro. -> (x) características da classe; (f) funções da classe 

# mago = Mago("Merlin", 4)
# arqueiro = Arqueiro("Legolas", 3)

# Usando métodos das classes
print(guerreiro.mostrar_status())  # Exibe status do Guerreiro
print(guerreiro.atacar())          # Guerreiro ataca

# print(mago.mostrar_status())       # Exibe status do Mago
# print(mago.atacar())               # Mago ataca

# print(arqueiro.mostrar_status())   # Exibe status do Arqueiro
# print(arqueiro.atacar())           # Arqueiro ataca
