# Resumidor de Artículos Web / Web Article Summarizer

## 📄 Descripción / Description

**ES:**  
Este proyecto permite resumir artículos de cualquier página web y generar un archivo PDF con el resumen. Utiliza inteligencia artificial para crear resúmenes automáticos y un diseño profesional en el PDF resultante.

**EN:**  
This project allows you to summarize articles from any website and generate a PDF file with the summary. It uses artificial intelligence for automatic summarization and produces a professionally formatted PDF.

---

## ⚙️ Stack Técnico / Tech Stack

- **Python 3.8+**
- [transformers (HuggingFace)](https://huggingface.co/docs/transformers/index) (modelo BART para resumen)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) (scraping de HTML)
- [Requests](https://docs.python-requests.org/) (descarga de páginas web)
- [FPDF](https://pyfpdf.github.io/fpdf2/) (generación de PDF)
- [Sumy](https://github.com/miso-belica/sumy) (opcional, para otros métodos de resumen)
- **Arial.TTF** (fuente personalizada para PDFs)

---

## 🚀 ¿Cómo funciona? / How does it work?

1. El usuario ejecuta el script con la URL de un artículo.
2. El programa descarga el texto del artículo.
3. Resume el contenido usando IA.
4. Genera un PDF con el resumen y lo guarda en la carpeta `output/`.

---

## 🛠️ Instalación / Installation

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/resumidor.git
   cd resumidor
   ```

2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   pip install transformers
   ```

3. Descarga y coloca el archivo `Arial.TTF` en el directorio principal del proyecto (necesario para los PDFs).

---

## ▶️ Uso / Usage

```sh
python main.py <URL-del-articulo>
```

Ejemplo:
```sh
python main.py https://blog.python.org/2024/04/awesome-features.html
```

El PDF generado se guardará en la carpeta `output/`.

---

## 📁 Estructura del Proyecto / Project Structure

```
resumidor/
│
├── main.py
├── scraper.py
├── summarizer.py
├── pdf_generator.py
├── utils.py
├── requirements.txt
├── Arial.TTF
├── output/
│   └── resumen_<url>_<fecha>.pdf
└── ...
```

---

## 📝 Notas / Notes

- El modelo de IA puede requerir una buena conexión a internet la primera vez (descarga automática).
- Si falta la fuente `Arial.TTF`, el script no podrá generar PDFs.
- El resumen es automático y puede variar en calidad según el artículo.
