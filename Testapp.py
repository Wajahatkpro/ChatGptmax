import streamlit as st
import requests
from io import BytesIO
from PIL import Image


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def apply_styled_image(url, prompt, model, iterations):
    payload = {
        "prompt": prompt,
        "model": model,
        "iterations": iterations,
        "url": url,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("https://fffiloni-stable-diffusion-img2img.hf.space/api/predict", json=payload, headers=headers)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    return img


# Set up the Streamlit app
st.set_page_config(page_title="Make Your Image Look AI", page_icon="🤖", layout="wide")
st.title("Make Your Image Look AI 😎")

# Allow the user to upload an image
st.sidebar.title("Upload an Image")
uploaded_image = st.sidebar.file_uploader("", type=["jpg", "jpeg", "png"])

# Allow the user to specify the style prompt and other parameters
st.sidebar.title("Set Parameters")
style_prompt = st.sidebar.text_input("Enter a style prompt")
model = st.sidebar.selectbox("Select a model", ["small", "medium", "large"])
iterations = st.sidebar.slider("Select the number of iterations", 1, 10, 1)

# Apply the style to the uploaded image
if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, use_column_width=True)

    if st.button("Apply Style"):
        with st.spinner("Applying Style..."):
            styled_image = apply_styled_image(uploaded_image, style_prompt, model, iterations)
            st.image(styled_image, use_column_width=True)
else:
    st.warning("Please upload an image to apply the style to.")
