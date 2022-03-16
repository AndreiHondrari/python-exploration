
from typing import (
    TYPE_CHECKING, Iterable,
)

from wsgiref.simple_server import make_server

if TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment


def application(
    environ: "WSGIEnvironment",
    start_response: "StartResponse",
) -> Iterable[bytes]:

    response_body = 'Dabadee dabadoo'

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain',),
        ('Content-Length', str(len(response_body)),),
    ]

    start_response(status, response_headers)

    return [response_body.encode()]


def main() -> None:
    httpd = make_server('127.0.0.1', 8000, application)
    httpd.handle_request()


if __name__ == "__main__":
    main()
