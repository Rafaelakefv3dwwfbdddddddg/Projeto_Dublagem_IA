from app.captura_audio import capturar_audio
from app.transcricao_whisper import transcrever_audio
from app.traducao import traduzir_texto
from app.gerador_voz import gerar_audio
from app.play_audio import tocar_audio

if __name__ == "__main__":
    caminho_audio = capturar_audio(duracao=10)
    texto = transcrever_audio(caminho_audio)
    traducao = traduzir_texto(texto)
    voz = gerar_audio(traducao)
    tocar_audio(voz)