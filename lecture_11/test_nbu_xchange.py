import os
import nbu_xchange
from nbu_xchange import convert_currency
from nbu_xchange import get_all_exchange_rates
from nbu_xchange import make_api_request


MOCK_RESPONSE = [
 {
"r030":826,"txt":"Фунт стерлінгів","rate":10,"cc":"GBP","exchangedate":"21.04.2025"
 },
 {
"r030":840,"txt":"Долар США","rate":8,"cc":"USD","exchangedate":"21.04.2025"
 },
 {
"r030":978,"txt":"Євро","rate":9,"cc":"EUR","exchangedate":"21.04.2025"
 },
 {
"r030":985,"txt":"Злотий","rate":2,"cc":"PLN","exchangedate":"21.04.2025"
 }
]



def test_get_all_exchange_rates(monkeypatch):
    try:
        os.remove("/tmp/cache")
    except:
        pass
    monkeypatch.setattr(nbu_xchange, "make_api_request", value=lambda url: MOCK_RESPONSE)
    expected = {"GBP": 10, "USD": 8, "EUR": 9, "PLN": 2}
    assert get_all_exchange_rates() == expected


def test_convert_currency_from_uah(monkeypatch):
    try:
        os.remove("/tmp/cache")
    except:
        pass
    mock_xrates = {"GBP": 10, "USD": 8, "EUR": 9, "PLN": 2}
    monkeypatch.setattr(nbu_xchange, "get_all_exchange_rates", value=lambda: mock_xrates)
    assert convert_currency("UAH", "PLN", 100) == 50


def test_convert_currency_to_uah(monkeypatch):
    try:
        os.remove("/tmp/cache")
    except:
        pass
    mock_xrates = {"GBP": 10, "USD": 8, "EUR": 9, "PLN": 2}
    monkeypatch.setattr(nbu_xchange, "get_all_exchange_rates", value=lambda: mock_xrates)
    assert convert_currency("USD", "UAH", 100) == 800
    assert convert_currency("EUR", "UAH", 100) == 900


def test_convert_currency_no_uah(monkeypatch):
    try:
        os.remove("/tmp/cache")
    except:
        pass
    mock_xrates = {"GBP": 10, "USD": 8, "EUR": 9, "PLN": 2}
    monkeypatch.setattr(nbu_xchange, "get_all_exchange_rates", value=lambda: mock_xrates)
    assert convert_currency("USD", "PLN", 100) == 400
