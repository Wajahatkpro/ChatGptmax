import streamlit as st
import requests
import json
from PIL import Image
import numpy as np

# Function to convert PIL image to numpy array
def pil_to_nparray(pil_image):
    return np.array(pil_image.getdata(), dtype=np.float32).reshape(pil_image.size[1], pil_image.size[0], -1)

# Function to convert numpy array to PIL image
def nparray_to_pil(np_array):
    return Image.fromarray(np.uint8(np_array))

# API endpoint URL
url = "https://api.stable.gpt3blender.com/api/v1/img2img/stablediffusion"

# Streamlit app
st.set_page_config(page_title="Image Transform App", page_icon=":art:")
st.title("Image Transform App")

# User inputs
prompt = st.text_input("Enter a prompt:", "Make the image look like it was painted by Van Gogh.")
input_file = st.file_uploader("Upload an input image:", type=["jpg", "jpeg", "png"])
output_size = st.slider("Output image size:", 128, 1024, 512, step=64)
strength = st.slider("Strength:", 0.0, 1.0, 0.8, step=0.1)
num_steps = st.slider("Number of steps:", 100, 5000, 1000, step=100)

# API payload
if input_file is not None:
    input_image = Image.open(input_file)
    input_array = pil_to_nparray(input_image)
    payload = {
        "prompt": prompt,
        "input": input_array.tolist(),
        "output_size": [output_size, output_size],
        "strength": strength,
        "num_steps": num_steps
    }

    # POST request to the API endpoint
    response = requests.post(url, data=json.dumps(payload))

    # Parse the response JSON
    response_data = json.loads(response.text)

    # Extract the transformed image array from the response
    output_array = np.array(response_data["output"])

    # Convert the transformed image array to PIL image
    output_image = nparray_to_pil(output_array)

    # Display the input and output images
    st.image(input_image, caption="Input Image", use_column_width=True)
    st.image(output_image, caption="Output Image", use_column_width=True)
