from urllib.parse import urlencode
import requests
import pandas as pd

BASE_URL = "http://history.openweathermap.org/data/2.5/history/city"


def get_api_request(api_key, params):
    """
    Call OpenWeatherMap historical weather API by coordinates
    Returns JSON file
    """
    query_dict = {"lat": params["lat"],
                  "lon": params["lon"],
                  "type": "hour",
                  "start": params["start"],
                  "end": params["end"],
                  "appid": api_key}

    query_str = urlencode(query_dict)

    api_request = requests.get(BASE_URL, query_str)

    return api_request.json()


def get_weather_history(api_key, params):
    """
    Extracts wind speed/direction data from JSON file
    Returns dataframe
    """

    weather_json = get_api_request(api_key, params)

    df = pd.DataFrame(data=weather_json["list"])

    df_return = pd.DataFrame(data=df["dt"])

    for col in df.columns[1:]:
        if isinstance(df[col][0], dict):
            temp_df = df[col].apply(pd.Series)
        elif isinstance(df[col][0], list):
            temp_df = df[col].apply(pd.Series)[0].apply(pd.Series)
        else:
            temp_df = df[col]
        df_return = df_return.join(temp_df)

    df_return["city_id"] = weather_json["city_id"]

    return df_return
