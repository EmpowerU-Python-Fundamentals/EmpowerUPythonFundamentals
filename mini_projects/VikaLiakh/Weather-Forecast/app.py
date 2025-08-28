import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

from weather_api import get_forecast
from file_handler import save_to_file, load_history

DEFAULT_CITIES = ["Chisinau", "Madrid", "Kyiv", "Amsterdam"]

st.set_page_config(page_title="🌤 Weather Project", page_icon="☁️")
st.title("🌍 Weekly Weather Forecast")

menu = st.radio("Choose Action:", ["Get Forecast", "See History"])

if menu == "Get Forecast":
    date_input = st.date_input("Select date:", datetime.now() + timedelta(days=1))
    date = date_input.strftime("%Y-%m-%d") # format yyyy-mm-dd
    hour = st.slider("Select hour for tomorrow:", 0, 23, 12)
    

    custom_city = st.text_input("Enter a city (optional):")
    if custom_city:
        cities = [custom_city]
    else:
        cities = DEFAULT_CITIES

    if st.button("Get Weather Data"):
        rows = []
        for city in cities:
            data = get_forecast(city, date, hour)
            if data:
                rows.append(data)

        
        df = pd.DataFrame(rows, columns=["City", "Date", "Hour", "MaxTemp (°C)", "MinTemp (°C)", "Humidity (%)", "WindSpeed (kph)", "WindDir"])
        st.dataframe(df, use_container_width=True)

        # Save results
        save_to_file(rows)
        st.success(f"✅ Results saved to 'forecast_results.txt'")

elif menu == "See History":
    df = load_history()
    if df is not None:
        st.table(df)  
    else:
        st.warning("No history file found yet. Run a forecast first.")
