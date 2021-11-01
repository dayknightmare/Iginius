# Iginius API 

## About

This is an API that searches data from the Central Bank of Brazil to make the Real Quotation for any other currency in a certain period of time.

## Requirements

If it's going to run on the Docker just have it installed, but if it's going to run locally it's necessary to have:

- Python >= 3.6
- PIP
- CassandraDB >= 3
- Linux or MacOS (recommended)

## Run

In your terminal, if you are going to run with Docker, run: 

```bash
docker-compose up
```

but if it's locally:

> **CassandraDB**

Follow the installation: [CassandraDB INSTALL](https://cassandra.apache.org/doc/latest/cassandra/getting_started/installing.html)


> **Python application**
>
> **Optional**

```bash

pip install virtualenv

virtualenv -p python3 env 

// OR

python3 -m venv env

```
> **Required**

```
pip install -r requirements.txt

python3 main.py
```

After that on port 8000 of the localhost the application will be available