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
            if response.status_code == 200:
                print(response.text)
            else:
                print("Not Found.")

    except requests.exceptions.ConnectionError:
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.INFO)
        logging.info("Connection error.")


if __name__ == '__main__':
    main()
