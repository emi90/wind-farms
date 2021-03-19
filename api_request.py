from urllib.parse import urlencode
from urllib.request import urlretrieve

BASE_URL = "http://history.openweathermap.org/data/2.5/history/city"
API_KEY = open("api_key.txt").read()


def get_history_weather(params):
    """
    Call OpenWeatherMap historical weather API by coordinates
    Returns JSON file
    """
    query_dict = {"lat": params["lat"],
                  "lon": params["lon"],
                  "type": "hour",
                  "start": params["start"],
                  "end": params["end"],
                  "appid": API_KEY}

    query_str = urlencode(query_dict)

    api_request = urlretrieve(BASE_URL, query_str)

    return api_request

