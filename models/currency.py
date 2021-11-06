from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
import datetime
import uuid


class Currency(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    date_created = columns.DateTime(default=datetime.datetime.now)
    date_search = columns.Date(primary_key=True)
    name = columns.Text(index=True)
    currency_id = columns.Integer(index=True)
    currency_code = columns.Integer(index=True)
    type = columns.Text(max_length=3)
    tax_buy = columns.Float()
    tax_sell = columns.Float()
    parity_buy = columns.Float()
    parity_sell = columns.Float()