import requests
import logging


CITIES = ["Лондон", "Шереметьево", "Череповец"]


def main():
    payload = {"nMTq": "", 'lang': 'ru'}

    try:
        for city in CITIES:
            url_template = 'https://wttr.in/{}'
            url = url_template.format(city)
            response = requests.get(url, params=payload)
            response.raise_for_status()
            print(response.text)

    except requests.exceptions.HTTPError:
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.INFO)
        logging.info("Not Found")
    except requests.exceptions.ConnectionError:
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.INFO)
        logging.info("Connection error")


if __name__ == '__main__':
    main()
