from domain.controller.currencies import router_currencies
from domain.controller.health import router_health
from cassandra.cqlengine import connection
from helpers.sync_models import sync
from fastapi import FastAPI


app = FastAPI()

connection.setup(
    ['iginius-cassandra-n1'], 
    "iginius", 
    protocol_version=3
)

sync()

app.include_router(router_health)
app.include_router(router_currencies)

if __name__ == "__main__":
    app.run()