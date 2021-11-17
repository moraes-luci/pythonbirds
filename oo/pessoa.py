class Pessoa:
    def cumprimentar (self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(Pessoa.cumprimentar(p))
    print(id(p))