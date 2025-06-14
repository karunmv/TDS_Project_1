import base64
from PIL import Image
import io
import pytesseract

def extract_text_from_base64(img_str):
    try:
        image_bytes = base64.b64decode(img_str)
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return ""
