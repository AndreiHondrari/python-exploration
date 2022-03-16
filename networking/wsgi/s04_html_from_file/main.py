
import pathlib
import logging

from typing import (
    TYPE_CHECKING, Iterable,
)

from wsgiref.simple_server import make_server
from wsgiref import headers as wsgi_headers

if TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment


logger = logging.getLogger()


def get_response_body() -> str:
    body = ''
    INDEX_PATH = pathlib.Path().absolute().joinpath("index.html")
    if INDEX_PATH.exists():
        with open(INDEX_PATH, "r") as pf:
            body = pf.read()
    else:
        logger.warn(f"Could not find {str(INDEX_PATH)}")

    return body


def application(
    environ: "WSGIEnvironment",
    start_response: "StartResponse",
) -> Iterable[bytes]:

    response_body = get_response_body()

    response_length = len(response_body)
    response_headers = wsgi_headers.Headers()
    response_headers.add_header('Content-Type', 'text/html')
    response_headers.add_header('Content-Length', str(response_length))

    status = '200 OK'

    start_response(status, response_headers.items())

    return [response_body.encode()]


def main() -> None:
    print("SERVER START")

    httpd = make_server('127.0.0.1', 8000, application)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Shutting down ...")
        httpd.server_close()

    print("SERVER STOP")


if __name__ == "__main__":
    main()
