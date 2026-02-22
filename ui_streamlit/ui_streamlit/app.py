import streamlit as st
from ui_streamlit.pages import dashboard, cliente, carteira, simulacao_acumulacao, simulacao_aposentadoria, sensibilidade, relatorio

st.set_page_config(page_title="WealthHive Hybrid", layout="wide")

menu = st.sidebar.radio("Menu:", ["Dashboard", "Clientes", "Carteira", "Simulação Acumulação", "Simulação Aposentadoria", "Sensibilidade", "Relatório"])

if menu == "Dashboard":
    dashboard.show()
elif menu == "Clientes":
    cliente.show()
elif menu == "Carteira":
    carteira.show()
elif menu == "Simulação Acumulação":
    simulacao_acumulacao.show()
elif menu == "Simulação Aposentadoria":
    simulacao_aposentadoria.show()
elif menu == "Sensibilidade":
    sensibilidade.show()
elif menu == "Relatório":
    relatorio.show()
