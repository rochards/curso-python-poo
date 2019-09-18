class Playlist2:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas # lembre que apenas um _, signfica que o atributo é protegido

    # isso se chama Duck typing
    def __getitem__(self, item): # forma de fazer com que a classe seja iterável
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    # Duck typing
    def __len__(self):
        return len(self._programas)

    # @property
    # def tamanho(self):
    #     return len(self._programas)