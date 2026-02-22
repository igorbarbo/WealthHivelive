import streamlit as st
from services.simulation_service import simulate_retirement

def show():
    st.title("Simulação Aposentadoria")
    current = st.number_input("Poupança atual", 0, 1000000, 10000)
    monthly = st.number_input("Contribuição mensal", 0, 100000, 1000)
    years = st.number_input("Anos até aposentadoria", 1, 50, 20)
    return_rate = st.number_input("Retorno anual esperado (%)", 0.0, 50.0, 7.0) / 100.0
    if st.button("Simular"):
        total = simulate_retirement(current, monthly, years, return_rate)
        st.write(f"Saldo projetado: {total:,.2f}")
