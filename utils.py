import base64
import io
from PIL import Image
import pytesseract

def extract_text_from_base64(img_b64: str) -> str:
    try:
        data = base64.b64decode(img_b64)
        image = Image.open(io.BytesIO(data))
        return pytesseract.image_to_string(image).strip()
    except Exception:
        return ""
