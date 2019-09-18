from programa import Programa

class Filme(Programa): # forma de dizer que Programa é classe mãe
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # chamando o construtor da classe mãe
        self.__duracao = duracao
    
    def __str__(self): # estamos sobrescrevendo esse método, pois já existe na classe mãe
        return f'Filme: { self._nome }, Ano: { self.ano }, Duração: {self.__duracao}, Likes: { self._likes }'

    @property
    def duracao(self):
        return self.__duracao