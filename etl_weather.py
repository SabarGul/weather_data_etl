import requests
import pandas as pd
from sqlalchemy import create_engine
from config import API_KEY, CITIES

# ----- Extract -----
def extract_weather_data(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    print(f"City: {city} - Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        # Adapted data structure
        current = data['current_condition'][0]
        return {
            'city': city,
            'temperature': current['temp_C'],
            'humidity': current['humidity'],
            'weather': current['weatherDesc'][0]['value']
        }
    else:
        return None

# ----- Transform -----
def transform_data(raw_data):
    df = pd.DataFrame([item for item in raw_data if item is not None])
    return df

# ----- Load -----
def load_to_db(df):
    engine = create_engine('sqlite:///weather_data.db')
    df.to_sql('weather', con=engine, if_exists='replace', index=False)
    print("Data loaded to database successfully.")

# ----- Main Run -----
if __name__ == "__main__":
    raw_data = [extract_weather_data(city) for city in CITIES]
    df = transform_data(raw_data)

    if df.empty:
        print("DataFrame is empty — skipping database write.")
    else:
        print(df.head())
        load_to_db(df)

 
