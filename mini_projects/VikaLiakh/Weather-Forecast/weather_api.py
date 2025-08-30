import requests


API_KEY = "YOUR_API_KEY"  # replace with your real key from weatherapi.com

def get_forecast(city: str, date: str, hour: int):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    try:
        response = requests.get(base_url, params={"key": API_KEY, "q": city, "days": 7})
        data = response.json()

        for day in data["forecast"]["forecastday"]:
            if day["date"] == date:
                min_temp = day["day"]["mintemp_c"]
                max_temp = day["day"]["maxtemp_c"]
                for hour_data in day["hour"]:
                    if hour_data["time"] == f"{date} {hour:02d}:00":
                        return [
                            city,
                            date,
                            f"{hour:02d}:00",
                            max_temp,
                            min_temp,
                            hour_data["humidity"],
                            hour_data["wind_kph"],
                            hour_data["wind_dir"]
                        ]
        return None
    except Exception as e:
        return [city, date, f"{hour:02d}:00", "", "", "", "", ""]
