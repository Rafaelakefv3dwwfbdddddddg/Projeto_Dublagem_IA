import sounddevice as sd
import numpy as np
import scipy.io.wavfile

def capturar_audio(duracao=10, nome_arquivo="audio_capturado.wav"):
    fs = 44100  # Frequência de amostragem
    print("🔴 Gravando áudio da tela...")
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()
    scipy.io.wavfile.write(nome_arquivo, fs, gravacao)
    print("✅ Áudio capturado salvo em", nome_arquivo)
    return nome_arquivo