import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from prompts import summarize_text

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        document = request.form["document"]
        response = summarize_text(document)
        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
