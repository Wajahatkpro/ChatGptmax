import stablediffusion
import streamlit as st
from PIL import Image

API_KEY = "your-api-key-goes-here"

def transform_image(prompt, image):
    if prompt and image:
        try:
            transformed_image = stablediffusion.generate(prompt, image, api_key=API_KEY)
            st.image(transformed_image, use_column_width=True)
        except:
            st.write("Error: Could not transform image with StableDiffusion API.")
    else:
        st.write("Error: Prompt or image not provided.")

def main():
    # Set page config
    st.set_page_config(page_title="Make your image look AI 😎", page_icon="🧑‍🎨", layout="wide", initial_sidebar_state="collapsed")

    # Add title
    st.title("Make your image look AI 😎")

    # Add upload option
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Add prompt input
    prompt = st.text_input("Enter a prompt...", max_chars=300)

    # Add transform button
    if st.button("Transform"):
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            transform_image(prompt, image)
        else:
            st.write("Error: No image file selected.")

if __name__ == '__main__':
    main()
