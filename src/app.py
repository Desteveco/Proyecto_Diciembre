from xspf_reader import xspf_reader
from aleatorizador import lista_aleatoria
from play_random_music import vlc_opener
ruta_xspf = 'D:/David/Programacion/Proyecto_Diciembre/Proyecto_Diciembre/songs/Playlist.xspf'
ruta_vlc = 'C:/Program Files/VideoLAN/VLC/vlc.exe'
rutas_musica = xspf_reader()
playlist = lista_aleatoria(rutas_musica)
vlc_opener(playlist, ruta_vlc)