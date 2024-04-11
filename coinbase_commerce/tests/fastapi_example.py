from coinbase_commerce import CoinbaseCommerceAPI
from fastapi import FastAPI, HTTPException, Request, Response

app = FastAPI()
api_key = "YOUR_API_KEY"
api = CoinbaseCommerceAPI(api_key=api_key)

@app.post("/coinbase/webhook")
async def handle_coinbase_webhook(request: Request):
    signature_header = request.headers.get('X-Cc-Webhook-Signature')
    request_body = await request.body()

    verification_result = api.webhook_signature_verification("YOUR_WEBHOOK_SECRET", request_body, signature_header)
    if verification_result == "Invalid Signature":
        raise HTTPException(status_code=400, detail="Invalid signature")

    event = await request.json()
    
    customer_id = event['event']['data']['metadata']['customer_id']
    customer_name = event['event']['data']['metadata']['customer_name']
    
    if event['event']['type'] == 'charge:confirmed': # You can add more checks if needed.
        embed = { # Sending to a discord webhook you can change this to what you want.
            "title": f"Payment Confirmation",
            "description": f"A ${event['event']['data']['pricing']['local']['amount']} Payment has been received for {event['event']['data']['name']}.",
            "color": 5793266,
            "footer": {"text": "Sanction Payment System"},
            "fields": [
                {
                    "name": "Transaction ID",
                    "value": f"{event['event']['data']['id']}",
                    "inline": False
                },
                {
                    "name": "UserID",
                    "value": customer_id,
                    "inline": True
                },
                {
                    "name": "Username",
                    "value": customer_name,
                    "inline": True
                }
            ]
        }

        async with httpx.AsyncClient() as client:
            await client.post("Discord-Webhook", json={"embeds": [embed]})     

    return Response(status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)
