from fpdf import FPDF
import os

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self._add_custom_font()

    def _add_custom_font(self):
        font_path = os.path.join(os.path.dirname(__file__), "Arial.TTF")
        if not os.path.exists(font_path):
            raise FileNotFoundError("⚠️ Falta el archivo Arial.TTF en el directorio del script.")
        self.add_font("ArialCustom", "", font_path, uni=True)
        self.set_font("ArialCustom", size=12)

def create_pdf(title, content, path):
    pdf = PDF()
    pdf.multi_cell(0, 10, f"Resumen de: {title}\n\n{content}")
    pdf.output(path)
