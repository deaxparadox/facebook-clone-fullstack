# required `waitress` for running

from waitress import serve
import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

from back.wsgi import application


if __name__ == "__main__":
    serve(
        app=application,
        host="127.0.0.1",
        port=8000,
        log=logger
    )