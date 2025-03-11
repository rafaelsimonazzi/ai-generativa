import openai
import os
import streamlit as st
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuração da página
st.set_page_config(page_title="Assistente de TI - Kaamp", layout="wide")

# Aplicando estilo com CSS personalizado
st.markdown(
    """
    <style>
        * {
            font-family: 'Segoe UI', sans-serif;
        }
        .stApp {
            background-color: #ffffff;
        }
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 80vh;
            text-align: center;
        }
        .title {
            font-size: 80px;
            font-weight: 600;
            font-family: 'Segoe UI Light', sans-serif;
            margin-bottom: 10px;
        }
        .highlight {
            font-size: 150px;
            font-weight: bold;
            font-family: 'Segoe UI', sans-serif;
            letter-spacing: -3px;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 60px;
            font-weight: 600;
            font-family: 'Segoe UI Light', sans-serif;
            margin-bottom: 40px;
        }
        .divider {
            width: 80%;
            height: 2px;
            background-color: #000;
            margin-bottom: 40px;
        }
        .input-box input {
            width: 940px;
            height: 65px;
            padding: 15px;
            font-size: 20px;
            font-family: 'Segoe UI Light', sans-serif;
            border-radius: 8px;
            border: 1px solid #ccc;
            background-color: #F8F8F8;
            color: #333333;
            text-align: center;
            outline: none;
        }
        ::placeholder {
            color: #666666;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Layout centralizado
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("""
    <p class='title'>Olá!</p>
    <div class='divider'></div>
    <p class='highlight'>Eu sou Kaamp,</p>
    <p class='subtitle'>seu Assistente de TI</p>
    """, unsafe_allow_html=True)

# Campo de entrada
user_input = st.text_input("", placeholder="No que posso te ajudar hoje?", key="user_input")

st.markdown("</div>", unsafe_allow_html=True)

# Se o usuário enviar uma mensagem, inicia o chat
if user_input:
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "system", "content": "Você é um assistente especialista em desenvolvimento de software e aplicativos."}
        ]
    
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state["messages"]
    )
    
    resposta = response["choices"][0]["message"]["content"]
    st.session_state["messages"].append({"role": "assistant", "content": resposta})
    
    st.write("""
    ---
    **Histórico da conversa:**
    """)
    for message in st.session_state["messages"]:
        role = "**Você:**" if message["role"] == "user" else "**Kaamp:**"
        st.write(f"{role} {message['content']}")