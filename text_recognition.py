import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')
    return text


def load_and_read_images(directory_path):
    for image in os.listdir(directory_path):
        image_path = os.path.join(directory_path, image)
        text = read_text_from_image(image_path)
        build_result = f"\nText from {image}:\n\n\n{text}\n" + 50 * "-"
        print(build_result)


if __name__ == "__main__":
    dir_path = "pics"
    load_and_read_images(dir_path)
