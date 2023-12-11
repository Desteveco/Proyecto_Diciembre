from xspf_reader import xspf_reader
from aleatorizador import lista_aleatoria
from play_random_music import vlc_opener
import os
ruta_xspf = 'C:/Users/Desteveco/Proyecto_Diciembre/Proembre/songs/playlist.xspf'
ruta_vlc = 'C:/Program Files/VideoLAN/VLC/vlc.exe'
def rutas_checker():
    global ruta_xspf, ruta_vlc
    if not os.path.exists(ruta_xspf):
        print(f"El archivo XSPF en la ruta '{ruta_xspf}' no existe.")
        nueva_ruta_xspf = input("Ingresa la ruta del archivo XSPF: ")
        if os.path.exists(nueva_ruta_xspf):
            ruta_xspf = nueva_ruta_xspf

    if not os.path.exists(ruta_vlc):
        print(f"La ruta de VLC en '{ruta_vlc}' no existe.")
        nueva_ruta_vlc = input("Ingresa la ruta de VLC: ")
        if os.path.exists(nueva_ruta_vlc):
            ruta_vlc = nueva_ruta_vlc
rutas_checker()
rutas_musica = xspf_reader(ruta_xspf)
playlist = lista_aleatoria(rutas_musica)
vlc_opener(playlist, ruta_vlc) 