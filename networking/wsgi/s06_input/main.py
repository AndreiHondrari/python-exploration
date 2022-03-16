
import pathlib
import logging
import string
from urllib import parse

from typing import (
    TYPE_CHECKING, List, Dict, Optional, cast, Iterable
)

from wsgiref.simple_server import make_server
from wsgiref import headers as wsgi_headers

if TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment

RequestMap = Dict[bytes, List[bytes]]

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


def get_response_body(
    request_number: int,
    submission_values_map: Optional[RequestMap] = None
) -> str:
    body = ''
    TEMPLATES_PATH = pathlib.Path().absolute().joinpath("templates")
    INDEX_PATH = TEMPLATES_PATH.joinpath("index.html")
    PART_1_PATH = TEMPLATES_PATH.joinpath("part_1.html")
    SUBMISSION_RES_PATH = TEMPLATES_PATH.joinpath("submission_result.html")

    if all([
        TEMPLATES_PATH.exists(),
        INDEX_PATH.exists(),
        PART_1_PATH.exists(),
        SUBMISSION_RES_PATH.exists(),
    ]):
        # -- get the templates --

        # index
        with open(INDEX_PATH, "r") as pf:
            body = pf.read()

        # part 1
        part_1 = ''
        with open(PART_1_PATH, "r") as pf:
            part_1 = pf.read()

        # submission result
        submission_result = 'No submission'
        if submission_values_map is not None:
            with open(SUBMISSION_RES_PATH, "r") as pf:
                submission_result = pf.read()

            sr_template = string.Template(submission_result)

            some_kek_vals = submission_values_map.get(b'some-kek', [])
            some_lol_vals = submission_values_map.get(b'some-lol', [])

            try:
                some_kek = some_kek_vals[0].decode()
            except IndexError:
                some_kek = 'N/A'

            try:
                some_lol = some_lol_vals[0].decode()
            except IndexError:
                some_lol = 'N/A'

            submission_result = sr_template.substitute({
                'some_kek': some_kek,
                'some_lol': some_lol,
            })

        # -- render the template --
        template = string.Template(body)
        body = template.substitute({
            'request_number': request_number,
            'part_1': part_1,
            'submission_result': submission_result,
        })
    else:
        logger.warn(f"Could not find {str(INDEX_PATH)}")

    return body


def handle_request(
    web_environment: "WSGIEnvironment",

) -> str:
    global request_count
    request_count += 1

    # get input
    try:
        request_body_size = int(web_environment.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0

    request_body = web_environment['wsgi.input'].read(request_body_size)
    request_map: Optional[RequestMap] = None

    if request_body_size:
        request_map = cast(Optional[RequestMap], parse.parse_qs(request_body))

    if request_map is not None and len(request_map) == 0:
        request_map = None

    if request_map is not None:
        print("REQUEST_BODY", request_map)
    else:
        print("NO_REQUEST_BODY")

    # render response
    response_body = get_response_body(request_count, request_map)

    return response_body


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

    response_body = handle_request(VALID_ENVIRONMENT_SETTINGS)

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
