import requests


OFFICES = ["Лондон", "Шереметьево", "Череповец"]


def main():
    for office in OFFICES:
        url_template = 'https://wttr.in/{}?nMTq&lang=ru'
        url = url_template.format(office)
        response = requests.get(url)
        print(response.text)


if __name__ == '__main__':
    main()
