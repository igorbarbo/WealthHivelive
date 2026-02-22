from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(file_name, title="Relatório WealthHive"):
    """
    Gera um PDF simples com título
    """
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, title)
    c.save()
