import requests


CITIES = ["Лондон", "Шереметьево", "Череповец"]


def main():
    for sity in CITIES:
        url_template = 'https://wttr.in/{}?nMTq&lang=ru'
        url = url_template.format(sity)
        response = requests.get(url)
        print(response.text)


if __name__ == '__main__':
    main()
