# Defining currency
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.74,
    'RS': 83.15
}

# Fuction for currency converting 
def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Invalid currency codes."


amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the source currency (e.g., USD): ").upper()
to_currency = input("Enter the target currency (e.g., EUR): ").upper()

result = convert_currency(amount, from_currency, to_currency)

if result != "Invalid currency codes.":
    print(f'{amount} {from_currency} is equal to {result} {to_currency}')
else:
    print("Invalid currency codes. Please check the currency codes you provided.")
