from coinbase_commerce import CoinbaseCommerceAPI

api_key = "YOUR_API_KEY"
api = CoinbaseCommerceAPI(api_key=api_key)

def create_charge():
    result = api.create_charge(name="Test Product", description="A test product", amount=100, customer_id=123, customer_name="John Doe")
    print(result) # Will return the charge url

def list_charges():
    charges = api.list_charges()
    print(charges)

def cancel_charge():
    charge_id = "CHARGE_ID"
    result = api.cancel_charge(charge_id=charge_id)
    print(result)

if __name__ == "__main__":
    create_charge()
    list_charges()
    cancel_charge()
