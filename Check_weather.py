import requests

def get_weather(city):
    # Step 1: Try environment variable
    api_key = "OPENWEATHER_API_KEY"

    # Step 2: If missing, ask user to paste it
    if not api_key:
        api_key = input("Enter your OpenWeather API key: ").strip()

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error for 4xx/5xx codes

        data = response.json()
        print(f"\n🌍 Weather in {city.capitalize()}:\n")
        print(f"🌡 Temperature: {data['main'].get('temp')}°C")
        print(f"☁ Condition: {data['weather'][0].get('description', '').capitalize()}")
        print(f"💧 Humidity: {data['main'].get('humidity')}%")
        print(f"💨 Wind Speed: {data['wind'].get('speed')} m/s")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("❌ Unauthorized: Check your API key.")
        elif response.status_code == 404:
            print("❌ City not found.")
        else:
            print(f"⚠️ HTTP error: {http_err}")
    except Exception as e:
        print("⚠️ Error fetching data:", e)

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)

