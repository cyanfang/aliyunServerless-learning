import json
import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from logger import init_logger

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
init_logger(app)

@app.route("/healthCheck")
def healthCheck():
    return "ok"


@app.route("/", methods=("GET", "POST"))
def index():
    try:
        if request.method == "POST":
            prompt = request.form["prompt"]
            app.logger.info("Get the input prompt is : {}".format(prompt))
            responseString = ""
            if prompt is not None:
                responseString = chat(prompt)
            return redirect(url_for("index", result=responseString))
        return render_template("index.html", result=request.args.get("result"))
    except Exception as e:
        app.logger.info(e)
        raise e


def chat(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    if response.choices:
        return response.choices[0].text
    return "API response error {}".format(json.dumps(response,indent=2))


if __name__ == '__main__':
    app.run()
