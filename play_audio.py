from pydub import AudioSegment
from pydub.playback import play

def tocar_audio(caminho_arquivo):
    print("▶️ Reproduzindo dublagem IA...")
    som = AudioSegment.from_file(caminho_arquivo, format="mp3")
    play(som)