import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = 'c4ca99f05aa76e7363a7cb94819b0792'

def get_weather(city):
    city = city.strip() 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description'].capitalize()
            humidity = data['main']['humidity']
            country = data['sys']['country']
            city_name = data['name']

            return f"📍 {city_name}, {country}\n🌡 Temperature: {temp}°C\n☁️ Weather: {desc}\n💧 Humidity: {humidity}%"
        elif response.status_code == 404:
            return "❌ City not found. Please try a valid city name."
        else:
            return f"⚠️ Error: {response.status_code} - Unable to fetch data."
    except Exception as e:
        return f"🚫 Network error: {str(e)}"

def show_weather():
    city = city_entry.get()
    if city.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    result = get_weather(city)
    result_label.config(text=result)

window = tk.Tk()
window.title("🌦 Weather App")
window.geometry("400x350")
window.configure(bg="white")

heading = tk.Label(window, text="Weather App", font=("Arial", 20, "bold"), bg="white", fg="blue")
heading.pack(pady=10)

city_entry = tk.Entry(window, font=("Arial", 14), width=30, justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Greater Noida")

get_btn = tk.Button(window, text="Get Weather", font=("Arial", 12), command=show_weather, bg="#007BFF", fg="white")
get_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), bg="white", justify="left")
result_label.pack(pady=10)

window.mainloop()
