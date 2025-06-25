from flask import Flask, request, jsonify
from scraper import get_article_text
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/resumir", methods=["POST"])
def resumir():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "Falta la URL"}), 400

    article = get_article_text(url)
    resumen = summarize_text(article)
    return jsonify({"resumen": resumen})

@app.route("/", methods=["GET"])
def home():
    return "✅ API de Resumidor corriendo."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
