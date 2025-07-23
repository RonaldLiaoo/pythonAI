import streamlit as st

number = st.number_input("請輸入數字", step=1, min_value=0, max_value=9)
st.text("數字金字塔")

for i in range(1, number + 1):
    st.write(str(i) * i)

st.text("----")

number2 = st.number_input("請輸入箭頭的層數", step=1, min_value=0, max_value=9)

pyramid = "箭頭金字塔：\n"

# 上半部箭頭
for i in range(1, number2 + 1):
    space = " " * (number2 - i)
    star = "*" * (2 * i - 1)
    pyramid += f"{space}{star}\n"

# 下半部箭頭
for i in range(1, number2 + 1):
    space = " " * (number2 - 1)
    star = "*"
    pyramid += f"{space}{star}\n"

# 顯示整體，用 code block 包住，保留空格與格式
st.write(f"```\n{pyramid}```")
