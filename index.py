import logging
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key =os.getenv("OPENAI_API_KEY")


@app.route("/healthCheck")
def healthCheck():
    return "ok"


@app.route("/", methods=["GET"])
def index2():
    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/add", methods=["POST"])
def index():
    prompt = request.form["prompt"]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=400,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return redirect(url_for("index", result=response.choices[0].text))

# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         prompt = request.form["prompt"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0.6,
#             max_tokens=400,
#             top_p=1.0,
#             frequency_penalty=0.0,
#             presence_penalty=0.0
#         )
#         return redirect(url_for("index", result=response.choices[0].text))
#
#     result = request.args.get("result")
#     return render_template("index.html", result=result)

