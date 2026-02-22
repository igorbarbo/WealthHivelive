from transformers import pipeline

# Inicializa analisador de sentimento
sentiment_en = pipeline("sentiment-analysis", model="finbert-tone")
sentiment_pt = pipeline("sentiment-analysis", model="pysentimiento/bert-base-portuguese-cased-financial")

def analyze_sentiment(text, lang='en'):
    """
    Retorna sentimento do texto
    lang: 'en' ou 'pt'
    """
    if lang == 'en':
        return sentiment_en(text)
    elif lang == 'pt':
        return sentiment_pt(text)
    else:
        return {"error": "Idioma não suportado"}
