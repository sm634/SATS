import os

import pdf2image.exceptions
from pdf2image import convert_from_path


def get_pdf_file_paths(dir_path='data/input/'):
    """
    Finds all pdf files in a directory and stores them in a list along with their relative path.
    :param dir_path: the directory to search for the pdf files.
    :return: list
        Returns a list of pdf documents and their paths.
    """
    pdf_files = os.listdir(dir_path)
    pdf_file_paths = [dir_path + file for file in pdf_files if '.pdf' in file]
    return pdf_file_paths


def get_pdf_names(dir_path='data/input/'):
    """
    Finds all pdf file names in a directory and stores them in a list along with their relative path.
    :param dir_path: the directory to search for the pdf files.
    :return: list
        Returns a list of pdf documents and their names.
    """
    pdf_files = os.listdir(dir_path)
    pdf_file_names = [file.replace('.pdf', '') for file in pdf_files if '.pdf' in file]
    return pdf_file_names


def save_images(pages, doc_name, output_dir='data/output/'):
    """
    Take in pdf to image converted pages and save them in a designated directory.
    :param pages: the input pdf pages converted to images to be saved
    :param doc_name: name of the document to save as.
    :param output_dir: the directory to save the output images.
    :return: output images
    """
    for i, page in enumerate(pages):
        image_name = f"{doc_name}_page_{i+1}.jpg"
        output_img = output_dir + image_name
        page.save(output_img, "JPEG")


pdfs_paths = get_pdf_file_paths()
pdf_names = get_pdf_names()

for j, pdf in enumerate(pdfs_paths):
    try:
        pages = convert_from_path(pdf)
        file_name = pdf_names[j]
        save_images(pages=pages, doc_name=file_name)
    except pdf2image.exceptions.PDFPageCountError:
        pass


