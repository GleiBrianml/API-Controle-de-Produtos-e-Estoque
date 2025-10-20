import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

#python -m streamlit run app.py

st.set_page_config(page_title="Gerenciador de Estoque", page_icon="🚛")
st.title("📦 Gerenciador de Estoque")

