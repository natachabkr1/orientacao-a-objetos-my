# Abstração - subjetivo

from abc import ABC, abstractmethod

# Classe abstrata Personagem
class Personagem(ABC):
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
    
    @abstractmethod
    def atacar(self):
        pass   # preciso definir nas subclasses

    @abstractmethod
    def usar_habilidade(self):
        pass
    
    def mostrar_status(self):
        return f"{self.nome} (Nível {self.nivel})"

# Subclasse para Guerreiro
class Guerreiro(Personagem):
    def atacar(self):
        return f"{self.nome} ataca com sua espada!"

    def usar_habilidade(self):
        return f"{self.nome} usa 'Golpe Poderoso'!"

# Subclasse para Mago
class Mago(Personagem):
    def atacar(self):
        return f"{self.nome} lança um feitiço!"

    def usar_habilidade(self):
        return f"{self.nome} usa 'Bola de Fogo'!"

# Subclasse para Arqueiro
class Arqueiro(Personagem):
    def atacar(self):
        return f"{self.nome} dispara uma flecha!"

    def usar_habilidade(self):
        return f"{self.nome} usa 'Tiro Preciso'!"

# Criando personagens
guerreiro = Guerreiro("Conan", 5)
mago = Mago("Merlin", 4)
arqueiro = Arqueiro("Legolas", 3)

# Exibindo status e usando métodos
print(guerreiro.mostrar_status())
print(guerreiro.atacar())
print(guerreiro.usar_habilidade())

print(mago.mostrar_status())
print(mago.atacar())
print(mago.usar_habilidade())

print(arqueiro.mostrar_status())
print(arqueiro.atacar())
print(arqueiro.usar_habilidade())
