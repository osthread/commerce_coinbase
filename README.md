# Coinbase Commerce Python SDK

`commerce_coinbase` is a modern, fully typed Python client for the [Coinbase Commerce API](https://commerce.coinbase.com/docs/api/) that stays current with the latest platform capabilities. Use it to integrate cryptocurrency payments into your product without wrestling with raw HTTP requests or manual signature verification.

## Why this library?

The official Coinbase Commerce wrapper is no longer maintained, leaving many new API capabilities inaccessible. This project aims to fill that gap by providing:

- ✅ **Complete coverage of core payment flows** – create, list, cancel charges, and retrieve events with minimal boilerplate.
- ✅ **First-class webhook utilities** – easily validate incoming events to keep your integration secure.
- ✅ **Pythonic ergonomics** – type hints, descriptive exceptions, and logical method names speed up integration and maintenance.

## Installation

Install from PyPI:

```bash
pip install commerce-coinbase
```

To work against a local checkout instead, clone the repository and install it in editable mode:

```bash
git clone https://github.com/maxiedev/Coinbase-Commerce.git
cd Coinbase-Commerce
pip install -e .
```

## Quick start

```python
from commerce_coinbase import CoinbaseCommerceAPI

# Authenticate with your Coinbase Commerce API key
api = CoinbaseCommerceAPI(api_key="YOUR_API_KEY")

# Create a one-time charge
charge = api.create_charge(
    name="Limited Edition Hoodie",
    description="Only 100 made",
    amount=20.00,
    currency="USD",
    pricing_type="fixed_price",
)

print(charge.code)  # Use this code to redirect customers to Coinbase Checkout
```

### Handling webhooks

```python
from commerce_coinbase.webhooks import CoinbaseWebhook

webhook = CoinbaseWebhook(shared_secret="YOUR_WEBHOOK_SHARED_SECRET")

def handle_event(request_body: bytes, signature: str):
    event = webhook.verify_signature(payload=request_body, signature=signature)
    # Process the event (e.g., mark charge as paid)
    return event
```

For a complete list of available methods, explore the `commerce_coinbase` package or check the [API reference](https://commerce.coinbase.com/docs/api/).

## Configuration tips

- **API key**: Generate a key from your Coinbase Commerce dashboard and keep it secret.
- **Timeouts & retries**: The client exposes `session` configuration if you need to customize request behavior for high-volume scenarios.
- **Environment variables**: In production environments, store credentials in variables such as `COINBASE_COMMERCE_API_KEY` and inject them at runtime.

## Development workflow

1. Install development dependencies with `pip install -r requirements.txt`.
2. Run the unit suite with `pytest` to validate changes.
3. Use `black` and `isort` (if installed) to maintain consistent formatting.

## Contributing

Contributions are welcome! Please:

1. Fork the repository and create a feature branch.
2. Add or update tests that cover your changes.
3. Submit a pull request describing your motivation and implementation details.

Before contributing, review the [CONTRIBUTING guidelines](CONTRIBUTING.md) for more information on project conventions.

## Community & support

Encounter a bug or need a feature? [Open an issue](https://github.com/maxiedev/Coinbase-Commerce/issues) with as much detail as possible. Discussions and suggestions are always appreciated.

## License

`commerce_coinbase` is distributed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for the full text.
