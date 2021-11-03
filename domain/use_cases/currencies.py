from domain.repository.currencies import save_currency_data, get_currencies_by_date_range
from helpers.currencies import processing_currency_data
from urllib3 import PoolManager
from typing import Union
import json


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
        currency_values.append(i.split(";"))

    return processing_currency_data(currency_values)


async def process_and_store_currencies(currency_values: list):
    dates = [i['date'] for i in currency_values]
    dates.sort()

    date_range = get_currencies_by_date_range(dates[len(dates) - 1], dates[0], currency_values[0]['name'])

    for i in currency_values:
        if str(i['date']) not in date_range:
            save_currency_data(
                date=i['date'],
                name=i['name'],
                currency_id=i['currency_id'],
                type=i['type'],
                tax_buy=i['tax_buy'],
                tax_sell=i['tax_sell'],
                parity_buy=i['parity_buy'],
                parity_sell=i['parity_sell']
            )


def get_json_currencies() -> list:
    with open("currencies.json", 'r') as f:
        js = json.loads(f.read())

    return js['currencies']