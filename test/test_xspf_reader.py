from src.xspf_reader import xspf_reader 

def test_2():
    ruta_xspf = 'C:/Users/Desteveco/Proyecto_Diciembre/Proyecto_Diciembre/songs/playlist.xspf' 
    rutas = xspf_reader(ruta_xspf)
    assert isinstance(rutas, list)  
    assert len(rutas) > 0  
