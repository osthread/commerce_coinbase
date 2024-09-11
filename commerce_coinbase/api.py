import httpx, hmac, hashlib

class CoinbaseCommerceAPI:
    def __init__(self, api_key):
        self.base_url = "api.commerce.coinbase.com"
        self.headers = {
            "X-CC-Api-Key": api_key, 
            "Content-Type": "application/json", 
            "Accept": "application/json",
        }

    def create_charge(self, name, description, amount, customer_id, customer_name, currency="USD", pricing_type="fixed_price"):
        """
        Create a charge via the Coinbase Commerce API.

        This function creates a new charge object with the specified details. It handles various errors by catching exceptions and raises a ValueError with an appropriate error message for errors related to the request or the response.

        Parameters:
            - name (str): The name of the product or service being charged for.
            - description (str): A description of the charge.
            - amount (float): The amount to be charged.
            - customer_id (int or str): The ID of the customer being charged.
            - customer_name (str): The name of the customer.
            - currency (str, optional): The currency in which the charge is made. Defaults to "USD".
            - pricing_type (str, optional): The pricing type of the charge. Defaults to "fixed_price".

        Returns:
            - str: The URL to the hosted payment page for the charge.
            - ValueError: If an error occurs during the request to the Coinbase Commerce API, such as a connection error, timeout, HTTP error, or if the response is not in the expected format.

        Examples:
            >>> api = CoinbaseCommerceAPI(api_key="your_api_key")
            >>> charge_url = api.create_charge(name="Test Product", description="A test product", amount=100, customer_id=123, customer_name="John Doe")
            >>> print(charge_url)
        """
        
        data = {
            "name": name,
            "description": description,
            "pricing_type": pricing_type,
            "local_price": {
                "amount": amount,
                "currency": currency
            },
            "metadata": {
                "customer_id": str(customer_id),
                "customer_name": str(customer_name)
            }
        }

        try:
            with httpx.Client() as client:
                response = client.post(f"https://{self.base_url}/charges", headers=self.headers, json=data)
                response.raise_for_status()
                charge_info = response.json()

                if 'data' in charge_info and 'hosted_url' in charge_info['data']:
                    return charge_info['data']['hosted_url']
                else:
                    return "Response from Coinbase Commerce is missing 'data' or 'hosted_url'."

        except httpx.HTTPStatusError as http_err:
            return f"HTTP error occurred: {http_err}. Response body: {response.text}"

        except httpx.RequestError as req_err:
            return f"Request error occurred: {req_err}"

        except ValueError as val_err:
            return val_err

        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def list_charges(self):
        """
        Retrieves a list of existing charges from the Coinbase Commerce API.

        This method makes a GET request to the Coinbase Commerce API to fetch the list of charges. It is designed to be used synchronously, blocking until the request is completed.

        Returns:
            dict: A dictionary object containing the list of charges and related information.
            ValueError: If an HTTP error occurs or there's an error in the request process.

        Example:
            >>> api = CoinbaseCommerceAPI(api_key="your_api_key")
            >>> charges = api.list_charges()
            >>> print(charges)
        """
        try:
            with httpx.Client() as client:
                response = client.get(f"https://{self.base_url}/charges", headers=self.headers)
                response.raise_for_status()
                charge_info = response.json()
                return charge_info

        except httpx.HTTPStatusError as http_err:
            return f"HTTP error occurred: {http_err}. Response body: {response.text}"

        except httpx.RequestError as req_err:
            return f"Request error occurred: {req_err}"

        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def cancel_charge(self, charge_id):
        """
        Cancels a charge via the Coinbase Commerce API.

        Parameters:
            charge_id (str): The unique identifier for the charge to cancel.

        Returns:
            dict: The response from Coinbase Commerce about the cancelled charge.
            ValueError: If an HTTP error occurs or there's an error in the request process.

        Example:
            >>> api = CoinbaseCommerceAPI(api_key="your_api_key")
            >>> result = api.cancel_charge(charge_id="charge_id")
            >>> print(result)
        """
        try:
            with httpx.Client() as client:
                response = client.post(f"https://{self.base_url}/charges/{charge_id}/cancel", headers=self.headers)
                response.raise_for_status()
                charge_info = response.json()
                return charge_info

        except httpx.HTTPStatusError as http_err:
            return f"HTTP error occurred: {http_err}. Response body: {response.text}"

        except httpx.RequestError as req_err:
            return f"Request error occurred: {req_err}"

        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def webhook_signature_verification(self, COINBASE_WEBHOOK_SECRET, request_body, signature_header):
        """
        Verifies the signature of a Coinbase Commerce webhook event to ensure it's valid and originated from Coinbase.

        This method compares the computed HMAC signature of the incoming webhook request's body against the provided signature in the 'X-Cc-Webhook-Signature' header. The Coinbase Commerce webhook secret is used as the key for HMAC SHA-256 hashing to compute the expected signature.

        Parameters:
            COINBASE_WEBHOOK_SECRET (str): The webhook secret provided by Coinbase Commerce, used for validating the signature.
            request_body (bytes): The raw body of the incoming webhook request. It's crucial to use the raw body without any alterations to ensure the hash matches correctly.
            signature_header (str): The signature obtained from the 'X-Cc-Webhook-Signature' header of the incoming request, to be verified against the computed signature.

        Returns:
            str: Returns "Invalid Signature" if verification fails, or "Signature Valid" if the verification is successful.

        FastAPI Example:
            >>> api = CoinbaseCommerceAPI(api_key="your_api_key")
        
            >>> @app.post("/coinbase/webhook")
            >>> async def handle_coinbase_webhook(request: Request):
            >>>     signature_header = request.headers.get('X-Cc-Webhook-Signature')
            >>>     request_body = await request.body()

            >>>     verification_result = api.webhook_signature_verification("COINBASE_WEBHOOK_SECRET", request_body, signature_header)
            >>>     if verification_result == "Invalid Signature":
            >>>         raise HTTPException(status_code=400, detail="Invalid signature")

            >>>     event = await request.json()
            
            >>>     customer_id = event['event']['data']['metadata']['customer_id']
            >>>     customer_name = event['event']['data']['metadata']['customer_name']

            >>>     if event['event']['type'] == 'charge:confirmed':
            >>>         embed = {
            >>>             "title": f"Payment Confirmation",
            >>>             "description": f"A ${event['event']['data']['pricing']['local']['amount']} Payment has been received for {event['event']['data']['name']}.",
            >>>             "color": 5793266,
            >>>             "footer": {"text": "Commerce Payment System"},
            >>>             "fields": [
            >>>                 {
            >>>                     "name": "Transaction ID",
            >>>                     "value": f"{event['event']['data']['id']}",
            >>>                     "inline": False
            >>>                 },
            >>>                 {
            >>>                     "name": "UserID",
            >>>                     "value": customer_id,
            >>>                     "inline": True
            >>>                 },
            >>>                 {
            >>>                     "name": "Username",
            >>>                     "value": customer_name,
            >>>                     "inline": True
            >>>                 }
            >>>             ]
            >>>         }

            >>>         async with httpx.AsyncClient() as client:
            >>>             await client.post("wehhook", json={"embeds": [embed]})     

            >>>     return Response(status_code=200)
        """
        expected_signature = hmac.new(bytes(COINBASE_WEBHOOK_SECRET, 'utf-8'), request_body, hashlib.sha256).hexdigest()

        if not hmac.compare_digest(signature_header, expected_signature):
            return "Invalid Signature"
        else:
            return "Signature Valid"
