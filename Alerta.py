import sounddevice as sd  # Importa a biblioteca para captura de áudio
import numpy as np  # Importa a biblioteca para manipulação de arrays
import time  # Importa a biblioteca para manipulação de tempo
import threading  # Importa a biblioteca para execução de tarefas em threads
import pygame  # Importa a biblioteca para reprodução de áudio

audio_playing = False  # Variável para controlar se o áudio está sendo reproduzido
audio_played = False   # Variável para controlar se o áudio foi reproduzido
threshold = 40      # Defina o limite de volume desejado

def audio_callback(indata, frames, time_info, status):
    global audio_playing, audio_played
    volume_norm = np.linalg.norm(indata) * 10  # Calcula o volume normalizado do áudio
    print("Volume atual:", volume_norm)
    time.sleep(0.1)  # Aguarda um curto período para evitar sobrecarga
    if volume_norm > threshold and not audio_playing:
        threading.Thread(target=play_alert_sound).start()  # Inicia a reprodução do alerta sonoro em uma nova thread
        audio_played = True
    elif volume_norm <= threshold:  
        audio_played = False

def play_alert_sound():
    global audio_playing
    audio_playing = True
    pygame.mixer.init()  # Inicializa o mixer do Pygame para reprodução de áudio
    pygame.mixer.music.load("Estágio.mp3")  # Carrega o arquivo de áudio
    pygame.mixer.music.play()  # Inicia a reprodução do áudio   
    while pygame.mixer.music.get_busy():  # Aguarda até que a reprodução do áudio seja concluída
        time.sleep(0.1)
    audio_playing = False  # Atualiza a variável para indicar que a reprodução foi concluída

def main():
    with sd.InputStream(callback=audio_callback):  # Inicia o monitoramento de áudio
        print("Iniciando monitoramento de áudio...")
        print("Pressione Ctrl+C para interromper o programa.")
        try:
            while True:
                pass  # Mantém o programa em execução
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuário.")

if __name__ == "__main__":
    main()
