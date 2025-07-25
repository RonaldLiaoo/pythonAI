# 海龜湯遊戲 多題

import streamlit as st
import openai
import json
import random

with open("question/quizzess.json", "r", encoding="utf-8") as f:
    quizzess = json.load(f)
    if "pick" not in st.session_state:
        st.session_state.pick = random.randrange(len(quizzess))
    quiz = quizzess[st.session_state.pick]

openai.api_key = st.secrets["OPENAI_API_KEY"]

system_message = f"你是海龜湯主持人，我會詢問問題，你只能回答(是/否/無關)，直到我的回答答案相近時說回答正確並給我完整答案，題目是：{quiz['question']}，答案是：{quiz['answer']}。"

st.title("海龜湯遊戲")

col1, col2 = st.columns([6, 1])
with col1:
    st.write(f"題目：  \n {quiz['question']}")
with col2:
    if st.button("🗑️"):
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
        model="gpt-4o",
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
