import datetime


def processing_currency_data(data: list) -> list:
    data_processed = []

    for i in data:
        if len(i) < 4:
            continue

        data_processed.append({
            'name': i[3],
            'date': datetime.datetime.strptime(i[0], "%d%m%Y").date(),
            'type': i[2],
            'currency_id': i[1],
            'tax_buy': float(i[4].replace(',', '.')),
            'tax_sell': float(i[5].replace(',', '.')),
            'parity_buy': float(i[6].replace(',', '.')) if len(i) > 6 else -1,
            'parity_sell': float(i[7].replace(',', '.')) if len(i) > 6 else -1,
        })

    return data_processed


def validate_and_tranform_date_str(date: str) -> str:
    try:
        d = datetime.datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        return ""

    return d.strftime("%d/%m/%Y")