from firebase_admin import firestore


class CurrencyRepository:

    collection = 'dolar_exchange'

    def __init__(self):
        db = firestore.client()
        self.ref = db.collection(self.collection)

    def find_all(self):
        return self.ref.stream()
    
    def find_by_currency(self, currency_id: str):
        return self.ref.where("currency", "==", currency_id).stream()
