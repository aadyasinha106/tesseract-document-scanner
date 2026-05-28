import pytesseract
from app.config import TESSERACT_CONFIG


def extract_text(image):
    text = pytesseract.image_to_string(
        image,
        config=TESSERACT_CONFIG
    )

    return text
