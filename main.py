import os
import argparse
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def is_bitlink(token, url):
    parsed_url = urlparse(url)
    link = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}" \
           f"{parsed_url.path}"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(link, headers=headers)
    return response.ok


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    payload = {
        "long_url": url,
        "domain": "bit.ly"
    }

    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten', headers=headers,
        json=payload
    )
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, link):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    parsed_link = urlparse(link)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}" \
          f"{parsed_link.path}/clicks/summary"

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    load_dotenv()
    token = os.getenv('BITLINK_ACCESS_TOKEN')

    parser = argparse.ArgumentParser(
        description='Программа принимает ссылки и возвращает на них битлинк.'
                    'Так же принимает битлинк и возвращает количество заходов '
                    'по ссылке'
    )
    parser.add_argument('url', help='Адрес сайта или битлинк')

    args = parser.parse_args()
    url = args.url

    try:
        if is_bitlink(token, url):
            print(f"Количество переходов по ссылке битли: "
                  f"{count_clicks(token, url)}")
        else:
            print(shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print('Вы ввели ссылку некорректного формата')


if __name__ == "__main__":
    main()
