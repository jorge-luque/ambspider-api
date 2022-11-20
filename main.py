from fastapi import FastAPI
from fastapi import FastAPI, Path, Query
import config
from currency_repository import CurrencyRepository

app = FastAPI()

config.init_firebase()

currency_repository = CurrencyRepository()

@app.get("/currencies")
async def root():
    collection: dict = currency_repository.find_all()
    currencies = []
    for doc in collection:
        currencies.append(doc.to_dict())
    return currencies

@app.get("/currencies/{currency_id}")
async def find_by_currency(
    currency_id: str = Path(title="The ID of the currency to get"),
):
    result: dict = currency_repository.find_by_currency(currency_id)
    ret = []
    for doc in result:
        ret.append(doc.to_dict())
    return ret
