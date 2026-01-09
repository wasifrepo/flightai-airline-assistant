import base64
from io import BytesIO
from PIL import Image

from app.config import IMAGE_MODEL
from app.services.openai_client import get_client


def generate_city_image(city: str) -> Image.Image:
    client = get_client()

    image_response = client.images.generate(
        model=IMAGE_MODEL,
        prompt=(
            f"An image representing a vacation in {city}, showing tourist spots and "
            f"everything unique about {city}, in a vibrant pop-art style"
        ),
        size="1024x1024",
        n=1,
        response_format="b64_json"
    )

    image_base64 = image_response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))
