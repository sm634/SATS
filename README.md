# SATS
Source Agnostic Text Summerizer (SATS). An application designed to automate text-based data extraction and summarisation in volumes.

### First Principles
1. Most communication over the internet happens through unstructured text.
2. To get an informed view regarding general trends based on feedback for a given topic (e.g. product, event, etc.), extraction of aggregated themes based on numerous documents of text will be invaluable. 

### Design overview
<img width="653" alt="image" src="https://user-images.githubusercontent.com/50050912/212035730-14192d3e-0c22-4070-88a8-72350b4837ab.png">

### Set-up

The environment used for this requires the installation of tesseract-ocr for text recognition. If you use windows, you can install it from here: 
https://github.com/UB-Mannheim/tesseract/wiki

You should take note of where the destination folder for the install location. It will likely look as follows: C:\Users\username\AppData\Local\Programs\Tesseract-OCR
This will be required when runnin Tesseract-OCR through the python script.
