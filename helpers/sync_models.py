from cassandra.cqlengine.management import sync_table
from models.currency import Currency


def sync():
    sync_table(Currency)