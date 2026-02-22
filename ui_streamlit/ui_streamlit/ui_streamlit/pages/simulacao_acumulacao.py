import streamlit as st
from services.simulation_service import monte_carlo_portfolio
import yfinance as yf

def show():
    st.title("Simulação Acumulação")
    ticker = st.text_input("Ticker para simulação", "AAPL")
    initial = st.number_input("Investimento inicial", 0, 1000000, 10000)
    periods = st.number_input("Dias de simulação", 1, 1000, 252)
    simulations = st.number_input("Número de simulações", 1, 5000, 1000)
    if st.button("Rodar Simulação"):
        df = yf.download(ticker)
        results = monte_carlo_portfolio(df['Close'], initial, periods, simulations)
        st.write("Resultados:", results[:10])
        st.line_chart(results)
