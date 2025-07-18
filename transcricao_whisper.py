import whisper

def transcrever_audio(caminho_arquivo):
    print("🔠 Transcrevendo com Whisper...")
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(caminho_arquivo)
    print("✅ Transcrição:", resultado["text"])
    return resultado["text"]