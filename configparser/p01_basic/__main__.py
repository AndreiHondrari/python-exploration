import configparser


def main() -> None:
    config = configparser.ConfigParser()
    config.read('stuff.ini')

    for k, v in config.items():
        print(k, v)

    print("KEK", config['DEFAULT']['Kek'])
    print("kekHUB", config['gandalf']['KekHub'])


if __name__ == "__main__":
    main()
