import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image
import io

load_dotenv()

def generate_image(prompt):
    api_key = os.getenv("HF_API_KEY")

    if not api_key:
        st.error("Please set your HF_API_KEY environment variable.")
        return None

    client = InferenceClient(
        provider="together",
        api_key=api_key,
    )

    try:
        image_bytes = client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-dev",
        )
        image = Image.open(io.BytesIO(image_bytes))
        return image
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.title("Text-to-Image Generator")

prompt = st.text_input("Enter your prompt:", "Hamster riding a turtle")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        generated_image = generate_image(prompt)
        if generated_image:
            st.image(generated_image, caption="Generated Image", use_column_width=True)
            #Save button to download the image.
            image_bytes = io.BytesIO()
            generated_image.save(image_bytes, format="PNG")
            st.download_button(
                label="Download Image",
                data=image_bytes.getvalue(),
                file_name="generated_image.png",
                mime="image/png",
            )