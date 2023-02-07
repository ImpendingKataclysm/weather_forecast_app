import requests

API_KEY = "b2389a6f2e887b5d8569b3ae113157fe"


def get_data(city_name, country_code, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Vancouver", "CA", 3))
