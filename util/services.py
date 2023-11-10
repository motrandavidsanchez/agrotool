import requests
from decouple import config


def weather_alerts() -> str:
    api_key = config('API_KEY', default='')
    city = config('CITY', default='San Fernando del valle de Catamarca')

    if not api_key:
        return 'Error: No se configuro la API KEY.'

    api_url = f'https://api.weatherbit.io/v2.0/alerts?key={api_key}&city={city}'

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            api_data = response.json()
            menssage = api_data.get('alerts')

            return menssage if menssage else 'No hay alerta meteorológica.'
        else:
            return 'Error al obtener datos de la API'

    except requests.exceptions.RequestException as e:
        return f'Error de conexión: {e}'
