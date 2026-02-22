import streamlit as st
from services.client_service import add_new_client, list_client_portfolios

def show():
    st.title("Clientes")
    with st.form("novo_cliente"):
        name = st.text_input("Nome do cliente")
        age = st.number_input("Idade", min_value=0, max_value=120)
        submitted = st.form_submit_button("Adicionar Cliente")
        if submitted:
            client = add_new_client(name, age)
            st.success(f"Cliente {client.name} adicionado com sucesso!")

    st.subheader("Carteiras por cliente")
    client_id = st.number_input("ID do cliente", min_value=1)
    if st.button("Mostrar Carteiras"):
        portfolios = list_client_portfolios(client_id)
        for p in portfolios:
            st.write(f"{p.name} (ID {p.id})")
