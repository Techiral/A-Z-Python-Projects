def convert_currency(amount, from_currency, to_currency):
    # Conversion rates (as of a specific date)
    conversion_rates = {
        ('USD', 'EUR'): 0.85,
        ('USD', 'GBP'): 0.74,
        ('EUR', 'USD'): 1.18,
        ('EUR', 'GBP'): 0.87,
        ('GBP', 'USD'): 1.35,
        ('GBP', 'EUR'): 1.15
    }

    if (from_currency, to_currency) in conversion_rates:
        return amount * conversion_rates[(from_currency, to_currency)]
    else:
        return None

# Get user input
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (USD, EUR, GBP): ").upper()
to_currency = input("Enter the currency to convert to (USD, EUR, GBP): ").upper()

# Convert currency
converted_amount = convert_currency(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
else:
    print("Invalid conversion. Please check the currencies you entered.")
