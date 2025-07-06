import streamlit as st

number = st.number_input("請輸入數字", step=1, min_value=0, max_value=9)
st.text("數字金字塔")

for i in range(1, number + 1):
    line = ""
    for j in range(i):
        line += str(i)
    st.write(line)

number2 = st.number_input("請輸入箭頭的層數", step=1, min_value=0, max_value=5)

pyramid = "箭頭金字塔：\n"

# 上半部金字塔
for i in range(1, number2 + 1):
    line = ""
    for j in range(5 - i):
        line += " "
    for j in range(2 * i - 1):
        line += "*"
    pyramid += line + "\n"

# 下半部箭頭（固定格式）
for i in range(1, number2 + 1):
    pyramid += "    *    \n"

# 顯示整體，用 code block 包住，保留空格與格式
st.write(f"```\n{pyramid}```")
