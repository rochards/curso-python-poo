from filme import Filme
from serie import Serie
from playlist import Playlist
from playlist2 import Playlist2

def run():
    vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
    for i in range(100):
        vingadores.dar_likes()

    edg = Filme('Era do gelo', 206, 130)
    for i in range(10):
        edg.dar_likes()

    atlanta = Serie('atlanta', 2018, 2)
    atlanta.dar_likes()

    tbbt = Serie('The big bang theory', 2008, 11)
    for i in range(50):
        tbbt.dar_likes()

    filmes_series = [vingadores, edg, tbbt, atlanta]
    for programa in filmes_series:
        print(programa) # o python já sabe que ele deve chamar o __str__

    print()
    print('from playlist')
    playlist = Playlist('fim de semana', filmes_series)
    for programa in playlist: # eu so posso iterar pq Playlist extends a classe list
        print(programa)
    print(f'Tamanho da lista: {len(playlist)}')
    print(f'TBBT em playlist? { tbbt in playlist }')

    print()
    print('from playlist')
    playlist2 = Playlist2('fim de semana', filmes_series)
    for programa in playlist2: # eu so posso iterar por causa do método __getitem__
        print(programa)
    print(f'Tamanho da lista: { len(playlist2) }') # só posso chamar o len por causa do método __len__
    print(f'TBBT em playlist2? { tbbt in playlist2 }')

if __name__ == '__main__':
    run()