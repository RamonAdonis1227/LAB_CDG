import pyaudio  # Importa a biblioteca PyAudio para lidar com entrada e saída de áudio
import numpy as np  # Importa a biblioteca NumPy para operações numéricas eficientes
import time  # Importa a biblioteca time para trabalhar com temporização
import threading  # Importa a biblioteca threading para lidar com threads
import pygame  # Importa a biblioteca Pygame para reprodução de áudio
import logging  # Importa a biblioteca logging para registro de mensagens de debug, info, etc.

# Configuração do logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('audio_monitor')

# Configuração do FileHandler para noise.txt
file_handler = logging.FileHandler('noise.txt')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

audio_playing = False  # Variável para controlar se o áudio está sendo reproduzido ou não
threshold = 40  # Defina o limite de volume desejado

# Função de callback que é chamada quando novos dados de áudio estão disponíveis
def audio_callback(in_data, frame_count, time_info, status):
    global audio_playing  # Usa a variável global audio_playing
    try:
        audio_data = np.frombuffer(in_data, dtype=np.float32)  # Converte os dados de áudio em formato NumPy
        volume_norm = np.linalg.norm(audio_data) * 10  # Calcula o volume normalizado dos dados de áudio
        logger.debug(f"Volume atual: {volume_norm}")  # Registra o volume atual
        time.sleep(0.1)  # Aguarda um curto período pra evitar sobrecarga

        # Verifica se o volume excede o threshold e se o áudio não está sendo reproduzido atualmente
        if volume_norm > threshold and not audio_playing:
            logger.error(f"Alerta de volume: {volume_norm}")  # Registra o alerta no arquivo noise.txt
            threading.Thread(target=play_alert_sound).start()  # Inicia uma nova thread para reproduzir o alerta
    except Exception as e:
        logger.error(f"Erro no callback de áudio: {e}")  # Registra erros que podem ocorrer no callback de áudio

    return (in_data, pyaudio.paContinue)  # Retorna os dados da entrada de áudio e indica que a monitoração deve continuar

# Função para reproduzir o alerta sonoro
def play_alert_sound():
    global audio_playing  # Usa a variável global audio_playing
    logger.debug("Iniciando reprodução de alerta")
    audio_playing = True  # Define que o áudio está sendo reproduzido

    try:
        pygame.mixer.init()  # Inicializa o mixer do Pygame para reprodução de áudio
        pygame.mixer.music.load("Alerta.mp3")  # Carrega o arquivo de áudio para reprodução
        pygame.mixer.music.play()  # Inicia a reprodução do áudio

        while pygame.mixer.music.get_busy():  # Aguarda até que a reprodução do áudio termine
            time.sleep(0.1)  # Aguarda um curto período pra evitar sobrecarga
    except Exception as e:
        logger.error(f"Erro ao reproduzir o áudio: {e}")  # Registra erros que podem ocorrer durante a reprodução do áudio
    finally:
        audio_playing = False  # Define que a reprodução do áudio terminou
        logger.debug("Reprodução de alerta concluída")

# Função principal do programa
def main():
    logger.info("Iniciando monitoramento de áudio...")  # Inicia o monitoramento de áudio
    logger.info("Pressione Ctrl+C para interromper o programa.")  # Informa ao usuário como interromper o programa

    try:
        p = pyaudio.PyAudio()  # Inicializa o objeto PyAudio para lidar com entrada e saída de áudio
        stream = p.open(format=pyaudio.paFloat32,  # Configura as propriedades do stream de entrada de áudio
                        channels=1,
                        rate=44100,
                        input=True,
                        stream_callback=audio_callback)

        stream.start_stream()  # Inicia a monitoração de áudio

        while stream.is_active():  # Mantém o programa em execução enquanto o stream de áudio está ativo
            time.sleep(1)  # Espera um segundo antes de verificar novamente se o stream está ativo

    except KeyboardInterrupt:
        logger.info("Programa interrompido pelo usuário.")  # Informa que o programa foi interrompido pelo usuário
    except Exception as e:
        logger.error(f"Erro no fluxo de entrada de áudio: {e}")  # Registra erros que podem ocorrer no fluxo de áudio
    finally:
        stream.stop_stream()  # Interrompe o stream de áudio
        stream.close()  # Fecha o stream de áudio
        p.terminate()  # Encerra a instância PyAudio
        logger.info("Monitoramento de áudio encerrado.")  # Informa o encerramento do monitoramento de áudio

if __name__ == "__main__":
    main()  # Chama a função principal do programa se este script for executado diretamente
