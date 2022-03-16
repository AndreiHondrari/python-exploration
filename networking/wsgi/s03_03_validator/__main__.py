
from typing import (
    TYPE_CHECKING, Iterable,
)

from wsgiref.simple_server import make_server
from wsgiref import validate as wsgi_validate

if TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment


request_count = 0


def application(
    environ: "WSGIEnvironment",
    start_response: "StartResponse",
) -> Iterable[bytes]:
    global request_count
    request_count += 1

    response_items = []

    environment_text = "\n".join([
        f"{k}: {v}"
        for k, v in environ.items()
    ]) + "\n" + ('-' * 50) + ("\n" * 3)

    response_items.append(environment_text.encode())

    main_response_body = f'Dabadee dabadoo Request number {request_count}'
    response_items.append(main_response_body.encode())

    status = '200 OK'

    total_length = [len(x) for x in response_items]
    response_headers = [
        ('Content-Type', 'text/plain',),
        ('Content-Length', str(total_length),),
    ]

    start_response(status, response_headers)

    return response_items


def main() -> None:
    print("SERVER START")

    validator_app = wsgi_validate.validator(application)

    httpd = make_server('127.0.0.1', 8000, validator_app)

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
