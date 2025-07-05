# weather_data_etl
# Weather Data ETL Project

This is a simple ETL (Extract, Transform, Load) pipeline that collects weather data from a public weather API and stores it in a local SQLite database.

## Features
- Extracts current weather for a list of cities using the [wttr.in](https://wttr.in) API (no API key required)
- Transforms the data into a structured format
- Loads it into a SQLite database for analysis

## Technologies
- Python
- Pandas
- SQLite
- Requests

## Setup

1. Clone the repository  
2. Create and activate a virtual environment (optional but recommended)  
3. Install dependencies:
```bash
pip install pandas sqlalchemy requests

## Setup
4. Run the script
```bash 
python etl_weather.py



