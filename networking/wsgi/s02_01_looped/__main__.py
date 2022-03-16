
from typing import (
    TYPE_CHECKING, Iterable,
)

from wsgiref.simple_server import make_server

if TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment


request_count = 0


def application(
    environ: "WSGIEnvironment",
    start_response: "StartResponse",
) -> Iterable[bytes]:
    global request_count
    request_count += 1

    response_body = f'Dabadee dabadoo Request number {request_count}'

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain',),
        ('Content-Length', str(len(response_body)),),
    ]

    start_response(status, response_headers)

    return [response_body.encode()]


def main() -> None:
    print("SERVER START")

    httpd = make_server('127.0.0.1', 8000, application)

    try:
        while True:
            httpd.handle_request()
    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Shutting down ...")
        httpd.server_close()

    print("SERVER STOP")


if __name__ == "__main__":
    main()
