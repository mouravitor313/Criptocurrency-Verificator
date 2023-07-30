import PySimpleGUI as sg
import requests
import time

def get_crypto_price(crypto_id, vs_currency):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': crypto_id,
        'vs_currencies': vs_currency,
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data[crypto_id][vs_currency]
        else:
            print(f"Erro ao obter o preço da criptomoeda. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

def get_price_history(crypto_id, vs_currency):
    url = 'https://api.coingecko.com/api/v3/coins/' + crypto_id + '/market_chart'
    params = {
        'vs_currency': vs_currency,
        'days': '5',  # Obtemos o histórico de preços dos últimos 5 dias
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['prices']
        else:
            print(f"Erro ao obter o histórico de preços da criptomoeda. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

def get_supported_cryptos():
    url = 'https://api.coingecko.com/api/v3/coins/list'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [crypto['id'] for crypto in data]
        else:
            print(f"Erro ao obter a lista de criptomoedas suportadas. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

if __name__ == "__main__":
    sg.theme('DarkPurple4')
    layout = [[sg.Text('CriptoChecker', font=('Helvetica', 24), text_color='white')],
              [sg.Text('Por: Vítor Moura', font=('Helvetica', 10), text_color='white')],
              [sg.Text('Digite o nome da criptomoeda que deseja verificar:')],
              [sg.Input(key='crypto_id')],
              [sg.Text('Digite a moeda para converter (como por exemplo: "usd" ou "brl"):')],
              [sg.Input(key='vs_currency')],
              [sg.Button('Verificar')],
              [sg.Button('Mostrar Criptomoedas Suportadas')],
              [sg.Text('', key='price_text')],
              [sg.Listbox([], size=(40, 5), key='price_history')],
              [sg.Listbox([], size=(40, 10), key='supported_cryptos')]]

    window = sg.Window('CriptoChecker', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Verificar':
            crypto_id = values['crypto_id']
            vs_currency = values['vs_currency']

            price = get_crypto_price(crypto_id, vs_currency)
            if price is not None:
                window['price_text'].update(f"Preço da criptomoeda {crypto_id.upper()} em {vs_currency.upper()}: {price}")

                price_history = get_price_history(crypto_id, vs_currency)
                if price_history is not None:
                    last_5_prices = price_history[-5:]
                    price_history_text = []
                    for timestamp, price in last_5_prices:
                        price_history_text.append(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp/1000))}: {price}")
                    window['price_history'].update(price_history_text)
                else:
                    window['price_text'].update("Não foi possível obter o histórico de preços da criptomoeda.")
            else:
                window['price_text'].update("Não foi possível obter o preço da criptomoeda.")
        elif event == 'Mostrar Criptomoedas Suportadas':
            supported_cryptos = get_supported_cryptos()
            if supported_cryptos is not None:
                window['supported_cryptos'].update(supported_cryptos)

    window.close()
