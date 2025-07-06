import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 載入 .env 檔案內容

# 設定 API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")

col1, col2, col3 = st.columns([6, 2, 1])
with col1:
    system_message = st.text_input("系統訊息", "請用繁體中文進行後續對話")
with col2:
    ai_model = st.selectbox("AI模型", ["gpt-4o-mini"])
with col3:
    if st.button("清除"):
        st.session_state.history = [{"role": "system", "content": system_message}]
        st.rerun()

# 初始化對話紀錄
if "history" not in st.session_state:
    st.session_state.history = [{"role": "system", "content": system_message}]

# 聊天輸入框
prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model=ai_model,
        messages=st.session_state.history,
    )

    assistant_message = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()

for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪄").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant", avatar="✨").write(message["content"])
