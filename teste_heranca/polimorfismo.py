# Polimorfismo - o mesmo método "atacar" pode ter comportamentos diferentes dependendo da classe do objeto
# Mesmo método com formas diferentes

# Classe base
class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
    
    def atacar(self):  # método subjetivo
        raise NotImplementedError("Este método deve ser sobrescrito pelas subclasses.")

# OU
#   def atacar(self):
#       pass  (método atacar genérico)

# Subclasse para Guerreiro
class Guerreiro(Personagem):
    def atacar(self):
        return f"{self.nome} ataca com uma espada! Dano: {self.nivel * 5}"

# Subclasse para Mago
class Mago(Personagem):
    def atacar(self):
        return f"{self.nome} lança uma bola de fogo! Dano: {self.nivel * 7}"

# Subclasse para Arqueiro
class Arqueiro(Personagem):
    def atacar(self):
        return f"{self.nome} dispara uma flecha! Dano: {self.nivel * 4}"

# Função que utiliza polimorfismo
def realizar_ataque(personagem):
    print(personagem.atacar())

# Criando personagens
guerreiro = Guerreiro("Conan", 5)
mago = Mago("Merlin", 4)
arqueiro = Arqueiro("Legolas", 3)

# Realizando ataques (Polimorfismo em ação)
realizar_ataque(guerreiro)  # Saída: Conan ataca com uma espada! Dano: 25
realizar_ataque(mago)       # Saída: Merlin lança uma bola de fogo! Dano: 28
realizar_ataque(arqueiro)   # Saída: Legolas dispara uma flecha! Dano: 12
