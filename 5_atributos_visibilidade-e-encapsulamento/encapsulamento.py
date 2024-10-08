# Encapsulamento
class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome  # atributo protegido
        self.profissao = profissao  # público
        self.__identidade = identidade  # atributo privado - não consegue alterar
    
    def __str__(self):
        return f'Nome: {self._nome}, Profissão: {self.profissao}, Identidade: {self.__identidade}'


pessoa1 = Pessoa('Marta Lima', 'Astronauta', '12345')
print(pessoa1)
print()

# Se tentarmos alterar um atributo público, nós vamos conseguir
pessoa1.profissao = 'Programadora'
print(pessoa1)
print()

# Se tentarmos alterar um atributo protegido, nós vamos conseguir também
pessoa1._nome = 'Marta'
print(pessoa1)
print()

# Ao tentar alterar um atributo privado, o valor não vai ser alterado
pessoa1.__identidade = '23525'
print(pessoa1)
print()