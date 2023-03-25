import json
import os
import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify
from openai import OpenAIError

from logger import init_logger

from werkzeug.exceptions import HTTPException

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
init_logger(app)

def handle_all_http_exception(error):
    status_code = getattr(error, 'code', 500)
    message = getattr(error, 'description', 'Internal Server Error')
    if status_code == 400:
        error_type = 'Bad Request'
    elif status_code == 401:
        error_type = 'Unauthorized'
    elif status_code == 403:
        error_type = 'Forbidden'
    elif status_code == 404:
        error_type = 'Not Found'
    elif status_code == 500:
        error_type = 'Internal Server Error'
    else:
        error_type = 'Unknown Error'

    response = jsonify({'error': message, 'status_code': status_code, 'error_type': error_type})
    response.status_code = status_code
    return response


@app.errorhandler(HTTPException)
def handle_all_exceptions(error):
    return handle_all_http_exception(error)

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
                app.logger.info("Get the responseString is : {}".format(responseString))
            return redirect(url_for("index", result=responseString))
        return render_template("index.html", result=request.args.get("result"))
    except OpenAIError as e:
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
        result = response.choices[0].text
    else:
        result = 'API response error {}".format(json.dumps(response, indent=2)'
    return {'status_code': '200', 'result': result}


if __name__ == '__main__':
    app.run()
