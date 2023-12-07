rutas = []
def xspf_reader():
    
    with open('D:/David/Programacion/Proyecto_Diciembre/Proyecto_Diciembre/songs/Playlist.xspf') as archivo_xspf:
        contenido = archivo_xspf.readlines()
        for linea in contenido:
            if '<location>' in linea:
                inicio = linea.find('<location>') + len('<location>')
                fin = linea.find('</location>')
                ruta = linea[inicio:fin]
                rutas.append(ruta)
    return rutas


