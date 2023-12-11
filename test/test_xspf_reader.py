from src.xspf_reader import xspf_reader
from src.xspf_reader import rutas

def test_1():
        assert isinstance(xspf_reader(), list)
def test_2():
        assert all(ruta.endswith('.mp3') for ruta in rutas)