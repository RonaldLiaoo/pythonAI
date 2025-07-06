import streamlit as st
import os

st.title("PythonAI課程")

folderPath = "markdown"
files = os.listdir(folderPath)
print(files)


st.markdown(
    """
一、網站架設流程：

1. 建立github專案

2. streamlit與github進行雲端連動

3. 使用VScode連接github專案

4. 上傳與更新網站
"""
)
st.write(" ")
st.markdown(
    """
二、如何更新網站：

1. 點選三角形 ▶

* 先自動存檔
* Black Formatter 幫你排版
* 執行程式

2. git上傳步驟

分享copilot進行提交與推送

3. 套用模組

開啟終端機輸入:streamlit run main.py

有Local URL跟全域網址，需要使用全域網址才可以分享，但可用Local URL來除錯

"""
)

print("Hello")
