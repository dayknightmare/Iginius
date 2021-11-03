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
    parity_buy: Optional[float],
    parity_sell: Optional[float],
):
    Currency.create(
        date=date,
        name=name,
        currency_id=currency_id,
        type=type,
        tax_buy=tax_buy,
        tax_sell=tax_sell,
        parity_buy=parity_buy,
        parity_sell=parity_sell,
    )


def get_currencies_by_date_range(date_end: datetime.date, date_start: datetime.date, currency: str) -> list:
    q = Currency.objects.filter(date__lte=date_end, date__gte=date_start, name=currency).only(['date', 'name']).allow_filtering()
    dates = []

    for i in q:
        dates.append(str(i.date))

    return dates