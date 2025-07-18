import requests
import os
from dotenv import load_dotenv

load_dotenv()

def gerar_audio(texto, nome_arquivo="voz_gerada.mp3"):
    api_key = os.getenv("ELEVEN_API_KEY")
    voice_id = os.getenv("VOICE_ID")
    print("🗣️ Gerando voz IA com ElevenLabs...")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": texto,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    resposta = requests.post(url, headers=headers, json=data)
    with open(nome_arquivo, "wb") as f:
        f.write(resposta.content)
    print("✅ Voz salva em", nome_arquivo)
    return nome_arquivo