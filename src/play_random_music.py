import subprocess
def vlc_opener(playlist, ruta_vlc):
    comando_vlc = [ruta_vlc] + playlist
    subprocess.Popen(comando_vlc)