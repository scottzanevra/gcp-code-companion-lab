
# create a webpage that allows you to lookup the weather forecast for a location using the weatherapi.com current weather api

import streamlit as st
import requests

# Set the API key
api_key = "YOUR_API_KEY"

# Create a function to get the weather forecast
def get_weather(city):
    # Make a request to the API
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        # Get the weather data
        data = response.json()

        # Get the current temperature
        current_temp = data["current"]["temp_c"]

        # Get the current weather condition
        current_condition = data["current"]["condition"]["text"]

        # Get the current wind speed
        current_wind_speed = data["current"]["wind_kph"]

        # Get the current humidity
        current_humidity = data["current"]["humidity"]

        # Return the weather forecast
        return f"The current temperature in {city} is {current_temp}°C. The current weather condition is {current_condition}. The current wind speed is {current_wind_speed} kph. The current humidity is {current_humidity}%."
    else:
        # Return an error message
        return "An error occurred while getting the weather forecast."

# Get the city from the user
city = st.text_input("Enter a city:")

# Get the weather forecast
weather_forecast = get_weather(city)

# Display the weather forecast
st.write(weather_forecast)