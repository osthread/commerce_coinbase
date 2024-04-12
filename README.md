# Coinbase Commerce

Since the official Coinbase Commerce API wrapper is no longer being actively updated and has become outdated, I decided to take the initiative to write my own and commit to keeping it up-to-date. `commerce_coinbase` is a comprehensive Python library that simplifies interactions with the Coinbase Commerce API, enabling developers to easily integrate cryptocurrency payments into their applications. With `commerce_coinbase`, you can create charges, list charges, cancel charges, and verify webhook signatures directly from your Python code.

## Features

- **Create Charges**: Quickly generate new charges for your products or services.
- **List Charges**: Retrieve a list of all created charges.
- **Cancel Charges**: Cancel pending charges.
- **Verify Webhook Signatures**: Ensure the integrity and origin of webhook events.

## Installation

Install `commerce_coinbase` via pip to get started:

```bash
git clone https://github.com/MaxieDev/Coinbase-Commerce.git
```

```bash
cd Coinbase-Commerce
```

```bash
python setup.py install
```

Note: This package is not yet available on PyPI. Installation instructions will be updated upon release.

## Getting Started

Here's how to create a new charge using `commerce_coinbase`:

```python
from commerce_coinbase import CoinbaseCommerceAPI

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

More examples on how to use `commerce_coinbase` can be found in the `tests` directory.

## Contributing

Contributions to `commerce_coinbase` are welcome! Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for more information on how to contribute to the project.

## License

`commerce_coinbase` is made available under the GPL-3.0 License. For more details, see the [LICENSE](LICENSE) file in the repository.

## Support and Contact

If you encounter any issues or have questions about `commerce_coinbase`, please file an issue on the [GitHub issues page](https://github.com/maxiedev/Coinbase-Commerce/issues).

---

Thank you for considering `commerce_coinbase` for your cryptocurrency payment needs. Happy coding!
