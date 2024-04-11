# Coinbase Commerce

Since the official Coinbase Commerce API wrapper is no longer being actively updated and has become outdated, I decided to take the initiative to write my own and commit to keeping it up-to-date. `coinbase_commerce` is a comprehensive Python library that simplifies interactions with the Coinbase Commerce API, enabling developers to easily integrate cryptocurrency payments into their applications. With `coinbase_commerce`, you can create charges, list charges, cancel charges, and verify webhook signatures directly from your Python code.

## Features

- **Create Charges**: Quickly generate new charges for your products or services.
- **List Charges**: Retrieve a list of all created charges.
- **Cancel Charges**: Cancel pending charges.
- **Verify Webhook Signatures**: Ensure the integrity and origin of webhook events.

## Installation

Install `coinbase_commerce` via pip to get started:

```bash
pip install coinbase_commerce
```

Note: This package is not yet available on PyPI. Installation instructions will be updated upon release.

## Getting Started

Here's how to create a new charge using `coinbase_commerce`:

```python
from coinbase_commerce import CoinbaseCommerceAPI

# Initialize the API with your Coinbase Commerce API key
api = CoinbaseCommerceAPI(api_key="your_api_key_here")

# Create a new charge
response = api.create_charge(
    name="Awesome T-Shirt",
    description="Limited edition T-Shirt",
    amount=20.00,
    customer_id=1,
    customer_name="Alice Bobson",
    currency="USD"
)

print(response)
```

## Documentation

For more detailed information about the Coinbase Commerce API's capabilities, visit the [official Coinbase Commerce API documentation](https://commerce.coinbase.com/docs/api/).

## Examples

More examples on how to use `coinbase_commerce` can be found in the `tests` directory.

## Contributing

Contributions to `coinbase_commerce` are welcome! Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for more information on how to contribute to the project.

## License

`coinbase_commerce` is made available under the MIT License. For more details, see the [LICENSE](LICENSE) file in the repository.

## Support and Contact

If you encounter any issues or have questions about `coinbase_commerce`, please file an issue on the [GitHub issues page](https://github.com/maxiedev/coinbase_commerce/issues).

---

Thank you for considering `coinbase_commerce` for your cryptocurrency payment needs. Happy coding!
