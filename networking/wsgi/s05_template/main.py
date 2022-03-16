
import pathlib
import logging
import string

from typing import (
    TYPE_CHECKING, Iterable,
)

from wsgiref.simple_server import make_server
from wsgiref import headers as wsgi_headers

if TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment


logger = logging.getLogger()

request_count = 0


def get_response_body(request_number: int) -> str:
    body = ''
    TEMPLATES_PATH = pathlib.Path().absolute().joinpath("templates")
    INDEX_PATH = TEMPLATES_PATH.joinpath("index.html")
    PART_1_PATH = TEMPLATES_PATH.joinpath("part_1.html")

    if all([
        TEMPLATES_PATH.exists(),
        INDEX_PATH.exists(),
        PART_1_PATH.exists(),
    ]):
        # get the template
        with open(INDEX_PATH, "r") as pf:
            body = pf.read()

        part_1 = ''
        with open(PART_1_PATH, "r") as pf:
            part_1 = pf.read()

        # render the template
        template = string.Template(body)
        body = template.substitute({
            'request_number': request_number,
            'part_1': part_1,
        })
    else:
        logger.warn(f"Could not find {str(INDEX_PATH)}")

    return body


def application(
    environ: "WSGIEnvironment",
    start_response: "StartResponse",
) -> Iterable[bytes]:
    global request_count
    request_count += 1

    response_body = get_response_body(request_count)

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
