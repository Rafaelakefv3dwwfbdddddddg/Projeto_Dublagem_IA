from googletrans import Translator

def traduzir_texto(texto, destino="pt"):
    print("🌍 Traduzindo texto...")
    tradutor = Translator()
    resultado = tradutor.translate(texto, dest=destino)
    print("✅ Tradução:", resultado.text)
    return resultado.text