import streamlit as st
import openai
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🤖 GPT 生成式 AI 聊天室")

# 初始化訊息：使用 GPT 對話格式（system/user/assistant）
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "請用繁體中文進行後續對話"}
    ]

# 顯示歷史訊息（略過 system ）
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 聊天輸入框
prompt = st.chat_input("請輸入訊息")

if prompt:
    # 顯示使用者訊息
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 呼叫 OpenAI API 取得回覆
    with st.chat_message("assistant"):
        with st.spinner("AI 正在回覆中..."):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o-mini",  # 或 gpt-3.5-turbo、gpt-4o
                    messages=st.session_state.messages,
                )
                reply = response.choices[0].message.content
                st.write(reply)
                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )
            except Exception as e:
                st.error(f"⚠️ 發生錯誤：{e}")
