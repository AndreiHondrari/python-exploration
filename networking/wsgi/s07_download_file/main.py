
import pathlib
import logging
import dataclasses as dc
from urllib import parse

from typing import (
    TYPE_CHECKING, List, Dict, Iterable
)

from wsgiref.simple_server import make_server
from wsgiref import headers as wsgi_headers
from wsgiref import util as wsgi_util

if TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment

RequestMap = Dict[bytes, List[bytes]]


@dc.dataclass(frozen=True)
class Response:
    headers: wsgi_headers.Headers
    body_items: Iterable[bytes]
    status: str


ENVIRONMENT_PREFIXES = [
    "SERVER",
    "QUERY",
    "wsgi",
    "HTTP",
    "CONTENT",
    "REMOTE",
    "GATEWAY",
    "PATH_INFO",
    "SCRIPT",
]

SEPARATOR = "\n" + ('-' * 50) + ("\n" * 3)


logger = logging.getLogger()

request_count = 0


def get_404(environ: "WSGIEnvironment") -> Response:
    error_message = "404 Missing page".encode()

    headers = wsgi_headers.Headers()
    headers.add_header('Content-Type', 'text/html; charset=utf-8')
    headers.add_header('Content-Length', str(len(error_message)))
    headers.add_header('Cache-Control', 'no-cache')
    headers.add_header('Server', '127.0.0.1:8000')

    return Response(
        headers=headers,
        body_items=[error_message],
        status='404 NOT FOUND'
    )


def get_index(
    environ: "WSGIEnvironment",
) -> Response:
    body = ''
    TEMPLATES_PATH = pathlib.Path().absolute().joinpath("templates")
    INDEX_PATH = TEMPLATES_PATH.joinpath("index.html")

    if INDEX_PATH.exists():
        with open(INDEX_PATH, "r") as pf:
            body = pf.read()
    else:
        logger.warn(f"Could not find {str(INDEX_PATH)}")

    body_bytes = body.encode()

    headers = wsgi_headers.Headers()
    headers.add_header('Content-Type', 'text/html')
    headers.add_header('Content-Length', str(len(body_bytes)))

    return Response(
        headers=headers,
        body_items=[body_bytes],
        status='200 OK'
    )


def get_something(
    environ: "WSGIEnvironment",
) -> Response:
    body = ''
    file_path = pathlib.Path().absolute().joinpath('something.txt')
    with open(file_path, "r") as pf:
        body = pf.read()

    body *= 5000

    body_bytes = body.encode()

    headers = wsgi_headers.Headers()
    headers.add_header('Content-Type', 'plain/text')
    headers.add_header('Content-Length', str(len(body_bytes)))
    headers.add_header(
        'Content-Disposition',
        "attachment; filename=potato.txt"
    )

    return Response(
        headers=headers,
        body_items=[body_bytes],
        status='200 OK'
    )


def get_favicon(
    environ: "WSGIEnvironment",
) -> Response:
    body_bytes = b''
    file_path = pathlib.Path().absolute().joinpath('potato.ico')
    with open(file_path, "rb") as pf:
        body_bytes = pf.read()

    headers = wsgi_headers.Headers()
    headers.add_header('Content-Type', 'image/x-icon')
    headers.add_header('Content-Length', str(len(body_bytes)))
    headers.add_header('Cache-Control', 'no-cache')

    return Response(
        headers=headers,
        body_items=[body_bytes],
        status='200 OK'
    )


URL_MAP = {
    '': get_index,
    '/potato': get_something,
    '/favicon.ico': get_favicon,
}


def handle_request(
    environ: "WSGIEnvironment",
) -> Response:
    # get URI
    request_uri = wsgi_util.request_uri(environ, include_query=False)

    parse_result: parse.ParseResult = parse.urlparse(request_uri)

    # obtain path (without trailin slash)
    url_path = parse_result.path
    if len(url_path) > 0:
        last_index = len(url_path) - 1
        if url_path[last_index] in ['/', '\\']:
            url_path = url_path[:last_index]

    print("SELECTED_URL_PATH: ", url_path)

    # dispatch
    request_handler = URL_MAP.get(url_path)
    if request_handler is None:
        response = get_404(environ)
    else:
        response = request_handler(environ)

    return response


def application(
    environ: "WSGIEnvironment",
    start_response: "StartResponse",
) -> Iterable[bytes]:

    VALID_ENVIRONMENT_SETTINGS = {
        k: v
        for k, v in environ.items()
        if any([
            k.startswith(prefix)
            for prefix in ENVIRONMENT_PREFIXES
        ])
    }

    response: Response = handle_request(VALID_ENVIRONMENT_SETTINGS)

    start_response(response.status, response.headers.items())

    return response.body_items


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
