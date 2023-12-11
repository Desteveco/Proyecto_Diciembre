rutas = []
def xspf_reader():
    with open('C:/Users/Desteveco/Proyecto_Diciembre/Proyecto_Diciembre/songs/playlist.xspf') as archivo_xspf:
        contenido = archivo_xspf.readlines()
        for linea in contenido:
            if '<location>' in linea:
                inicio = linea.find('<location>') + len('<location>')
                fin = linea.find('</location>')
                ruta = linea[inicio:fin]
                if ruta.endswith('.mp3'):
                    rutas.append(ruta)
                else:
                    print(f"Mi programa codeado en una semana y media no admite otros archivos que no sean .mp3, asi que tu archivo '{ruta}' no estara en la playlist, lo siento :D")
    return rutas
