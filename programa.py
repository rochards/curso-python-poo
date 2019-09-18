class Programa:
    def __init__(self, nome, ano, likes = 0):
        self._nome = nome.title() # com apenas um _ nós dizemos que o atributo é protected
        self.ano = ano
        self._likes = likes

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property # funciona como um gatter
    def nome(self):
        return self._nome
    
    @nome.setter # setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self): # imagine como se fosse o toString do java
        return f'Nome: { self._nome }, Ano: { self.ano }, Likes: { self._likes }'