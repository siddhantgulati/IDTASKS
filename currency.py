import requests

# Replace 'YOUR_API_KEY' with your Fixer.io API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = f'https://data.fixer.io/api/latest?access_key={API_KEY}'

def get_exchange_rates(base_currency):
    try:
        response = requests.get(BASE_URL)
        data = response.json()
        rates = data['rates']
        return rates
    except Exception as e:
        print("Error:", e)
        return None

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount

    if from_currency != 'EUR':
        amount_in_eur = amount / exchange_rates[from_currency]
    else:
        amount_in_eur = amount

    converted_amount = amount_in_eur * exchange_rates[to_currency]
    return converted_amount

def main():
    print("Currency Converter")
    print("------------------")

    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    from_currency = input("Enter the currency you have (e.g., EUR): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., GBP): ").upper()
    amount = float(input("Enter the amount to convert: "))

    exchange_rates = get_exchange_rates(base_currency)
    
    if exchange_rates:
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()
