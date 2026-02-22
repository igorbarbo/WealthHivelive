import streamlit as st
from services.portfolio_service import create_new_portfolio

def show():
    st.title("Carteira")
    with st.form("nova_carteira"):
        client_id = st.number_input("ID do cliente", min_value=1)
        name = st.text_input("Nome da carteira")
        tickers = st.text_area("Ativos (TICKER:quantidade), linha por linha")
        submitted = st.form_submit_button("Criar Carteira")
        if submitted:
            assets = {}
            for line in tickers.split("\n"):
                if ":" in line:
                    ticker, qty = line.split(":")
                    assets[ticker.strip()] = float(qty.strip())
            portfolio = create_new_portfolio(client_id, name, assets)
            st.success(f"Carteira {portfolio.name} criada com sucesso!")
