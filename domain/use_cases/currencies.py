from helpers.currencies import processing_currency_data
from domain.repository.currencies import save_currency_data
from urllib3 import PoolManager
from typing import Union


def get_api_currency() -> list:
    http = PoolManager()

    try:
        r = http.request("GET", "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=222&DATAINI=24/07/2021&DATAFIM=23/08/2021")
        data = r.data.decode()

    except Exception:
        return [-1]

    data = data.split('\n')

    currency_values = []

    for i in data:
        currency_values.append(i.split(";"))

    currency_values = processing_currency_data(currency_values)

    for i in currency_values:
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

    return currency_values