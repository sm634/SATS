import os
from flask import redirect, render_template, request, url_for
from forms import UploadFile
from prompts import summarize_text
import openai
from flask import Flask
from werkzeug.utils import secure_filename
import pdf2image.exceptions
from pdf2image import convert_from_path
from decouple import config

import pytesseract
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # required for crf secret token of the form.
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config['IMAGE_FOLDER'] = app.config['UPLOAD_FOLDER'] + '/converted_images/'
app.config['SUMMARIES_FOLDER'] = app.config['UPLOAD_FOLDER'] + '/summaries/'

openai.api_key = config("OPENAI_API_KEY")

pytesseract.pytesseract.tesseract_cmd = config("PYTESSERACT_PATH")

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        document = request.form["document"]
        response = summarize_text(document)
        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/upload", methods=('GET', 'POST'))
def upload():
    form = UploadFile()
    if form.validate_on_submit():
        filename = request.files['file'].filename

        # only allow files with the approved extensions to be uploaded.
        if allowed_file(filename):
            file = form.file.data  # first grab the file
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config['UPLOAD_FOLDER'],
                                   secure_filename(file.filename)))

            if get_file_extension(filename) == 'pdf':
                # remove extension of filename
                filename = filename.replace(r' ', '_')
                # convert pdf to image
                pdf_pages = convert_from_path(app.config['UPLOAD_FOLDER'] + f'/{filename}')
                # save image from pdf.
                filename = filename.replace('.pdf', '')
                image_path = app.config['IMAGE_FOLDER'] + f'{filename}'
                for page in pdf_pages:
                    page.save(image_path, "JPEG")

                # use ocr to extract image from text.
                text = pytesseract.image_to_string(Image.open(image_path))
                response = summarize_text(text)

                summary_txt_path = app.config['SUMMARIES_FOLDER'] + f'{filename}.txt'
                with open(summary_txt_path, 'w') as f:
                    f.write(response)
                    f.close()

                return render_template("upload.html", form=form, result=response)

        else:
            redirect(url_for("upload"))

    return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
