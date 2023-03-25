from flask import abort, jsonify
from werkzeug.exceptions import HTTPException

from index import app


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

    response = jsonify({'error': {}, 'status_code': status_code, 'type': error_type, 'message': message})
    response.status_code = status_code
    return response


@app.errorhandler(HTTPException)
def handle_all_exceptions(error):
    return handle_all_http_exception(error)