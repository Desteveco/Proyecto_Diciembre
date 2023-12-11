from src.aleatorizador import lista_aleatoria

def test_lista_aleatoria():
    rutas = ['cancion1.mp3', 'cancion2.mp3', 'cancion3.mp3']
    resultado = lista_aleatoria(rutas)

    assert isinstance(resultado, list)

