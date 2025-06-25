from scraper import get_article_text
from summarizer import summarize_text
from pdf_generator import create_pdf
import sys
import os
from utils import get_today_string, sanitize_filename

def main():
    if len(sys.argv) < 2:
        print("📌 Uso: python main.py <URL>")
        return

    url = sys.argv[1]
    print(f"🔎 Procesando URL: {url}")

    article = get_article_text(url)
    resumen = summarize_text(article)
    filename = f"resumen_{sanitize_filename(url)}_{get_today_string()}.pdf"

    output_path = os.path.join("output", filename)
    create_pdf(url, resumen, output_path)

    print(f"✅ PDF generado: {output_path}")

if __name__ == "__main__":
    main()
