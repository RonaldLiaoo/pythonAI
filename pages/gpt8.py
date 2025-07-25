import streamlit as st
import openai
import base64

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("AI 圖像生成 (GPT-Image-1)")


st.header("從文字提示生成圖像")

size = st.selectbox(
    "圖像尺寸",
    ["1024x1024", "1536x1024", "1024x1536", "auto"],
    help="方形圖片生成速度最快，預設為 1024x1024 像素",
)

quality = st.selectbox(
    "圖像品質",
    ["auto", "low", "medium", "high"],
    help="品質越高，生成時間越長，費用也越高",
)

output_format = st.selectbox(
    "輸出格式", ["png", "jpeg", "webp"], help="選擇圖像輸出格式"
)

background = st.selectbox(
    "背景選項", ["auto", "transparent"], help="透明背景僅適用於 PNG 或 WebP 格式"
)

if background == "transparent" and output_format == "jpeg":
    st.warning("JPEG 格式不支援透明背景，請選擇 PNG 或 WebP 格式")

if output_format in ["jpeg", "webp"]:
    output_compression = st.slider(
        "壓縮率",
        min_value=0,
        max_value=100,
        value=75,
        help="值越低檔案越小，但品質越差",
    )

prompt_text = st.text_area("提示詞", "A cute baby sea otter")

moderation = st.selectbox(
    "審核嚴格程度", ["auto", "low"], help="auto 為標準過濾，low 為較寬鬆的過濾"
)

if st.button("開始生成圖片"):
    with st.spinner("正在生成圖片，請稍候..."):
        try:
            params = {
                "model": "gpt-image-1",
                "prompt": prompt_text,
                "n": 1,
                "size": size,
                "quality": quality,
            }

            if background != "auto":
                params["background"] = background

            generatedImage = openai.images.generate(**params)

            image_base64 = generatedImage.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            st.image(image_bytes)

            token_cost = {
                "1024x1024": {"low": 272, "medium": 1056, "high": 4160},
                "1024x1536": {"low": 408, "medium": 1584, "high": 6240},
                "1536x1024": {"low": 400, "medium": 1568, "high": 6208},
            }

            if quality != "auto" and size != "auto":
                try:
                    est_tokens = token_cost[size][quality]
                    st.info(f"預估使用約 {est_tokens} 個圖像 token，加上少量文字 token")
                except:
                    pass

            st.download_button(
                label="下載圖片",
                data=image_bytes,
                file_name=f"generated_image.{output_format}",
                mime=f"image/{output_format}",
            )

        except Exception as e:
            st.error(f"生成圖片時發生錯誤: {e}")
