import os

import pdf2image.exceptions
from pdf2image import convert_from_path


pdf = convert_from_path('data/input/pdfs/107-EPD-Invoice-00197864.pdf'
                        ,poppler_path='C:/Users/safmuk01/AppData/Local/anaconda3/pkgs/poppler-23.01.0/Library/bin'
                        )
breakpoint()
