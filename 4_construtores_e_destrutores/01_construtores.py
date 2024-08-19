# Construtor Padrão
class MinhaClasse1:
    def __init__(self):
        print('MinhaClasse1: Chamou o construtor padrão')

class MinhaClasse2:
    pass  # não faz nada


# Construtor Parametrizado
class MinhaClasse3:
    def __init__(self, parametro):
        print(f'MinhaClasse3: Chamou o construtor parametrizado com o parâmetro {parametro}')



objeto1 = MinhaClasse1()
objeto2 = MinhaClasse2()
objeto3 = MinhaClasse3('meu objeto')

