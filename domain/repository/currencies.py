from models.currency import Currency
from typing import Optional
import datetime


def save_currency_data(
    date: datetime.date,
    name: str,
    currency_id: int,
    type: int,
    tax_buy: float,
    tax_sell: float,
    currency_code: int,
    parity_buy: Optional[float],
    parity_sell: Optional[float],
):
    Currency.create(
        date_search=date,
        name=name,
        currency_id=currency_id,
        type=type,
        tax_buy=tax_buy,
        tax_sell=tax_sell,
        parity_buy=parity_buy,
        parity_sell=parity_sell,
        currency_code=currency_code,
    )


def get_currencies_dates_by_date_range(date_end: str, date_start: str, currency: str) -> list:
    q = Currency.objects.filter(date_search__lte=date_end, date_search__gte=date_start, name=currency).only(['date_search', 'name']).allow_filtering()
    dates = []

    for i in q:
        dates.append(str(i.date_search))

    return dates


def get_currencies_by_two_dates(date_end: str, date_start: str, currency_code: int) -> list:
    q = Currency.objects.filter(date_search__lte=date_end, date_search__gte=date_start, currency_code=currency_code).allow_filtering()

    data = []

    for i in q:
        data.append(dict(i))

    return data


def get_currencies_by_two_dates_count(date_end: str, date_start: str, currency_code: int) -> list:
    q = Currency.objects.filter(
        date_search__lte=date_end, 
        date_search__gte=date_start, 
        currency_code=currency_code
    ).only(['id']).allow_filtering()

    c = 0

    for i in q:
        c += 1

    return c


def check_if_currencies_has_two_dates(date_end: str, date_start: str, currency_code: int) -> list:
    q = Currency.objects.filter(
        date_search__in=[date_end, date_start], 
        currency_code=currency_code
    ).only(['id']).allow_filtering()

    print(q)

    c = 0
    for i in q:
        c += 1

    return c == 2