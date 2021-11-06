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
            'currency_code': i[8],
        })

    return data_processed


def processing_currency_data_from_db(data: list) -> list:
    data_processed = []

    for i in data:
        if len(i) < 4:
            continue

        data_processed.append({
            'name': i['name'],
            'date': str(i['date_search']),
            'type': i['type'],
            'currency_id': i['currency_id'],
            'tax_buy': i['tax_buy'],
            'tax_sell': i['tax_sell'],
            'parity_buy': i['parity_buy'],
            'parity_sell': i['parity_sell'],
            'currency_code': i['currency_code'],
        })

    return sorted(data_processed, key=lambda x: x['date'])


def validate_and_tranform_date_str(date: str) -> str:
    try:
        d = datetime.datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        return ""

    return d.strftime("%d/%m/%Y")


def get_next_working_day(date: datetime.datetime, ceiling: bool = True) -> datetime.datetime:
    days_add = 0
    
    if date.weekday() in [5, 6] and ceiling:
        days_add = 7 - date.weekday()

    elif date.weekday() in [5, 6]:
        days_add = 4 - date.weekday()

    return date + datetime.timedelta(days=days_add)