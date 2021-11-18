class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar (self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    lucineia = Pessoa(nome='lucineia')
    daniel = Pessoa(lucineia,nome='Daniel')
    print(daniel.cumprimentar())
    print(Pessoa.cumprimentar(daniel))
    print(id(daniel))
    print(daniel.nome)
    print(daniel.idade)
    for filho in daniel.filhos:
        print(filho.nome)
        daniel.sexo = 'Masculino'
        del daniel.filhos
        print(daniel.sexo)
        print(daniel.__dict__)
        print(lucineia.__dict__)
        print(lucineia.olhos)
