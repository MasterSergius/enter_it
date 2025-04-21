import math
import json
import fire
import requests
from ttl_cache import ttl_disk_cache


API_URL="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


def make_api_request(api_url):
    response = requests.get(url=api_url)
    return response.json()


@ttl_disk_cache("/tmp/cache", 3600)
def get_all_exchange_rates():
    data = make_api_request(API_URL)
    return {item["cc"]: item["rate"] for item in data}


def convert_currency(currency_from: str, currency_to: str, amount: float) -> float:
    xrates = get_all_exchange_rates()
    if currency_from == "UAH":
        return round(amount / xrates[currency_to], 2)

    if currency_to == "UAH":
        return round(amount * xrates[currency_from], 2)

    return round(amount * xrates[currency_from] / xrates[currency_to], 2)


if __name__ == "__main__":
    fire.Fire(convert_currency)
