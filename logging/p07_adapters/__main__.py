
import sys
import logging

from typing import MutableMapping, Any, Tuple


class KekAdapter(logging.LoggerAdapter):

    def process(
        self,
        msg: str,
        kwargs: MutableMapping[str, Any]
    ) -> Tuple[str, MutableMapping[str, Any]]:
        return (f"[__ {self.extra['special_id']} __]:{msg}", kwargs,)


def main() -> None:
    default_formatter = logging.Formatter(logging.BASIC_FORMAT)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(default_formatter)

    kek = logging.getLogger("kek")

    kek.addHandler(stream_handler)

    kek_adapter_1 = KekAdapter(kek, {'special_id': 1234})
    kek_adapter_2 = KekAdapter(kek, {'special_id': 9876})

    kek_adapter_1.critical("WHAAAATT")
    kek_adapter_2.critical("THE THING OF THE THING")


if __name__ == "__main__":
    main()
