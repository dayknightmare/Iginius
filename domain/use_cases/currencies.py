from domain.repository.currencies import (
    save_currency_data, 
    get_currencies_dates_by_date_range, 
    get_currencies_by_two_dates, 
    get_currencies_by_two_dates_count,
    check_if_currencies_has_two_dates
)

from helpers.currencies import processing_currency_data, get_next_working_day, processing_currency_data_from_db
from urllib3 import PoolManager
from typing import Union
import datetime
import json
import math


async def get_api_currency(
    id_currency: int,
    start_date: str,
    final_date: str,
) -> list:
    http = PoolManager()

    try:
        r = http.request(
            "GET", 
            f"https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda={id_currency}&DATAINI={start_date}&DATAFIM={final_date}"
        )
        data = r.data.decode()

    except Exception:
        return [-1]

    data = data.split('\n')
    currency_values = []

    for i in data:
        currency_values.append([*i.split(";"), id_currency])

    return processing_currency_data(currency_values)


async def get_data_currency(
    id_currency: int,
    start_date: str,
    final_date: str,
) -> list:
    start_date_working_day = get_next_working_day(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
    final_date_working_day = get_next_working_day(datetime.datetime.strptime(final_date, "%d/%m/%Y"), False)

    if datetime.datetime.now() < final_date_working_day:
        final_date_working_day = get_next_working_day(datetime.datetime.now(), False)

    diff_date = (final_date_working_day - start_date_working_day).days
    diff_date -= (math.ceil(diff_date / 7) * 2) + (math.ceil(diff_date / 7) * 0.4)

    if check_if_currencies_has_two_dates(str(final_date_working_day.date()), str(start_date_working_day.date()), id_currency):
        q_rows = get_currencies_by_two_dates_count(str(final_date_working_day.date()), str(start_date_working_day.date()), id_currency)

        if q_rows >= diff_date:
            return processing_currency_data_from_db(
                get_currencies_by_two_dates(
                    str(final_date_working_day.date()), 
                    str(start_date_working_day.date()), 
                    id_currency
                )
            )

    return await get_api_currency(id_currency, start_date, final_date)
    

async def process_and_store_currencies(currency_values: list):
    dates = [i['date'] for i in currency_values]
    dates.sort()

    date_range = get_currencies_dates_by_date_range(dates[len(dates) - 1], dates[0], currency_values[0]['name'])

    for i in currency_values:
        if str(i['date']) not in date_range:
            save_currency_data(
                date=i['date'],
                name=i['name'],
                currency_id=i['currency_id'],
                type=i['type'],
                tax_buy=i['tax_buy'],
                tax_sell=i['tax_sell'],
                currency_code=i['currency_code'],
                parity_buy=i['parity_buy'],
                parity_sell=i['parity_sell'],
            )


def get_json_currencies() -> list:
    with open("currencies.json", 'r') as f:
        js = json.loads(f.read())

    return js['currencies']