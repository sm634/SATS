import os


import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\safmuk01\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def img_to_txt(input_dir='data/input/images/',
               output_dir='data/output/from_images/'):
    """
    A function that grabs all input images, uses ocr from tesseract-ocr to convert them to text and saves them as a txt
    file in an output folder.
    :param input_dir: the input directory containing the images to be converted to text.
    :param output_dir: the output directory to save the converted text data into
    :return: text
    """
    file_extensions = ['.jpg', '.png']
    images_file = os.listdir(input_dir)
    for file in images_file:
        file_path = input_dir + file
        text = pytesseract.image_to_string(Image.open(file_path))
        # replace the extensions to text.
        for ext in file_extensions:
            if ext in file:
                file = file.replace(ext, '.txt')
        with open(output_dir + file, 'w') as f:
            f.write(text)
            f.close()
        print(f"image {file} converted to text and saved.")


img_to_txt()
