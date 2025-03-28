import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

api_key = os.getenv("HF_API_KEY")

client = InferenceClient(
    provider="together",
    api_key=api_key,
)

image = client.text_to_image(
    "Hamster riding a turtle",
    model="black-forest-labs/FLUX.1-dev",
)

image.show()
image.save("gen_image.png")