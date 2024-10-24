import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != "404":
            main = data["main"]
            wind = data["wind"]
            weather_desc = data["weather"][0]["description"]

            # Extract and format weather data
            temperature = main["temp"]
            humidity = main["humidity"]
            pressure = main["pressure"]
            wind_speed = wind["speed"]

            weather_data = (
                f"City: {city}\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Pressure: {pressure} hPa\n"
                f"Wind Speed: {wind_speed} m/s\n"
                f"Description: {weather_desc.capitalize()}"
            )
            result_label.config(text=weather_data)
        else:
            messagebox.showerror("Error", "City not found!")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")

# Function to handle the search button click
def search_weather():
    city = city_entry.get()
    if city:
        get_weather(city)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Creating the main window
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("400x400")
root.config(bg="lightblue")

# Title Label
title_label = tk.Label(root, text="Weather Dashboard", font=("Helvetica", 18, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Entry field for city name
city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 12), bg="lightblue")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
city_entry.pack(pady=5)

# Button to search for weather
search_button = tk.Button(root, text="Search Weather", command=search_weather, font=("Helvetica", 12), bg="green", fg="white")
search_button.pack(pady=10)

# Label to display weather result
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="lightblue", justify="left")
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
