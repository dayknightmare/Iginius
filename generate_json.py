import json


with open("./currencies_raw.txt", 'r') as f:
    lines = f.readlines()

currencies = {
    "currencies": []
}

for i in lines:
    plain = i.replace('\n', '').replace('\r', '').replace('\t', '')
    code, currency = plain.split(" ", 1)

    currencies['currencies'].append({
        "name": currency,
        "code": code
    })


with open('currencies.json', 'w') as f:
    json.dump(currencies, f, indent=4)