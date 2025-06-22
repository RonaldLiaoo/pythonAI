import streamlit as st
import openai
from dotenv import load_dotenv
import os

# 載入 .env 環境變數
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化對話紀錄（完整 messages）
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "請用繁體中文進行後續對話"}
    ]

# 顯示歷史對話
for msg in st.session_state.messages[1:]:  # 跳過 system 訊息
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 輸入框
prompt = st.chat_input("請輸入訊息")

if prompt:
    # 顯示使用者訊息
    with st.chat_message("user"):
        st.markdown(prompt)
    # 加入訊息到 messages
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 呼叫 OpenAI API 回覆
    with st.chat_message("assistant"):
        with st.spinner("AI 回覆中..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # 或 gpt-4o
                    messages=st.session_state.messages,
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )
            except Exception as e:
                st.error(f"⚠️ 發生錯誤：{e}")
