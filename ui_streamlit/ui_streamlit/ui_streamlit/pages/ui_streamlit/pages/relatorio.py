import streamlit as st
from utils.pdf_generator import generate_pdf

def show():
    st.title("Relatório")
    filename = st.text_input("Nome do arquivo PDF", "relatorio.pdf")
    if st.button("Gerar PDF"):
        generate_pdf(filename)
        st.success(f"PDF {filename} gerado com sucesso!")
