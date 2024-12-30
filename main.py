import requests


CITIES = ["Лондон", "Шереметьево", "Череповец"]


def request_weather(city):
    payload = {"nMTq": "", 'lang': 'ru'}

    url_template = 'https://wttr.in/{}'
    url = url_template.format(city)
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.text


def main():
    try:
        for city in CITIES:
            print(request_weather(city))
    except requests.exceptions.HTTPError:
        print("Not Found.")
    except requests.exceptions.ConnectionError:
        print("Connection error.")


if __name__ == '__main__':
    main()
