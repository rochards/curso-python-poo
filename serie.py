from programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) # chamando o construtor da classe mãe
        self.__temporadas = temporadas

    def __str__(self): # estamos sobrescrevendo esse método, pois já existe na classe mãe
        return f'Série: { self._nome }, Ano: { self.ano }, Temporadas: {self.__temporadas}, Likes: { self._likes }'

    @property
    def temporadas(self):
        return self.__temporadas