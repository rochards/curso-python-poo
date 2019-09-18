''' A desvatagem de fazer dessa forma, é que você não conhece todo o comportamento da classe
list, assim, também não conhecerá por inteiro a classe Playlist. 
Veja a classe Playlist2 '''
class Playlist(list): # extendendo para a classe list
    def __init__(self, nome, programas):
        super().__init__(programas)
        self.nome = nome.title()