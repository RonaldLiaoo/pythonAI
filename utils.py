import streamlit as st

def load_openai_api() -> str:
    """
    加載 OpenAI API 金鑰。
    Returns:
        str: OpenAI API 金鑰。
    Raises:
        RuntimeError: 如果未找到 OpenAI API 金鑰。
    """

    openai_api_key = st.secrets["OPENAI_API_KEY"]
    if not openai_api_key:
        st.error("未找到 OpenAI API 金鑰。請設置環境變數 OPENAI_API_KEY。")
        st.stop()
    return openai_api_key
