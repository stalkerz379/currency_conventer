import requests
import json
from functools import lru_cache


def get_currency_cost() -> tuple[dict, dict]:
    try:
        user_currency = input('Enter the the currency you have as a shorten version. (E.g. "USD", "EUR".) \n').lower()
        url = f'http://www.floatrates.com/daily/{user_currency}.json'
        response = requests.get(url)
        json_data: dict = json.loads(response.content)
        inverse_rate_usd = extract_currency_rate(json_data, 'usd')
        inverse_rate_eur = extract_currency_rate(json_data, 'eur')
        cached_currencies = {'usd': inverse_rate_usd, 'eur': inverse_rate_eur}
        return json_data, cached_currencies
    except json.decoder.JSONDecodeError:
        print('Wrong currency name, try again')
        return get_currency_cost()


def validate_user_input(json_data: dict) -> tuple[str, float]:
    try:
        currency_exchange_on = input('Menu:\nType exit/!exit to close the program.\nOr select the currency you want to get the rate of:\n').lower().strip()
        if currency_exchange_on == '!exit' or currency_exchange_on == 'exit':
            print('Bye!')
            exit()
        amount_of_money = float(input('Enter amount of money you want to exchange:\n'))
        if amount_of_money < 0 or currency_exchange_on not in json_data.keys():
            raise ValueError
        else:
            return currency_exchange_on, amount_of_money
    except ValueError:
        print('Wrong input, try again')
        return validate_user_input(json_data)


def calculate_rate(amount_of_money: int | float, inverse_rate: int | float, currency_name: str) -> None:
    print(f'You received {round(amount_of_money * inverse_rate, 2)} {currency_name.upper()}.')


def extract_currency_rate(json_data: dict, currency_name: str) -> float:
    for key in json_data.keys():
        if key == currency_name:
            currency_obj = json_data[currency_name]
            inverse_rate = currency_obj['rate']
            return inverse_rate


def main():
    json_data, cached_currencies = get_currency_cost()
    for _ in json_data.keys():
        currency_exchange_on, amount_of_money = validate_user_input(json_data)
        inverse_rate_user_curr = extract_currency_rate(json_data, currency_exchange_on)
        print('Checking the cache...')
        if currency_exchange_on == 'usd' or currency_exchange_on == 'eur'\
                or currency_exchange_on in cached_currencies.keys():
            print('Oh! It is in the cache!')
            calculate_rate(amount_of_money, inverse_rate_user_curr, currency_exchange_on)
        else:
            print('Sorry, but it is not in the cache!')
            calculate_rate(amount_of_money, inverse_rate_user_curr, currency_exchange_on)
            cached_currencies.setdefault(currency_exchange_on, inverse_rate_user_curr)


if __name__ == '__main__':
    main()


