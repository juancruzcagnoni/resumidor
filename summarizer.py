from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

MAX_INPUT_CHARS = 3000  

def summarize_text(text, max_length=500, min_length=300): 
    if len(text) < 50:
        return "❗ Texto demasiado corto para resumir."

    text = text.strip().replace("\n", " ")

    if len(text) > MAX_INPUT_CHARS:
        text = text[:MAX_INPUT_CHARS]

    summary = summarizer_pipeline(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )
    return summary[0]['summary_text']
