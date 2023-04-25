import tkinter as tk
import json
import requests


def get_weather():
    temperature_d = {}
    wind_speed_d = {}
    wind_direction_d = {}
    humidity_d = {}
    pressure = {}
    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop/format/json")
    if response.status_code == 200:
        print(type(response.content))
        data = json.loads(response.content)
        for i in range(len(data)):
            station = data[i]['stacja']
            temperature_d[station] = data[i]['temperatura']
            wind_speed_d[station] = data[i]['predkosc_wiatru']
            wind_direction_d[station] = data[i]['kierunek_wiatru']
            humidity_d[station] = data[i]['wilgotnosc_wzgledna']
            pressure[station] = data[i]['cisnienie']
    try:

        temperature_label.config(text=f"Temperature in {entry.get()}: {temperature_d[entry.get()]}",
                                 background=None)
        wind_speed_label.config(text=f"Wind speed in {entry.get()}: {wind_speed_d[entry.get()]}")
        wind_direction_label.config(text=f"Wind direction in {entry.get()}: {wind_direction_d[entry.get()]}")
        humidity_label.config(text=f"Humidity in {entry.get()}: {humidity_d[entry.get()]}")
        pressure_label.config(text=f"Pressure in {entry.get()}: {pressure[entry.get()]}")
    except KeyError:
        temperature_label.config(text="Try again", background="red")


root = tk.Tk()
root.geometry("400x400")
root.title("Weather")

# elements
entry = tk.Entry(root)
button = tk.Button(root, text="show temperature", command=get_weather)
temperature_label = tk.Label(root, text="Temperature: ")
wind_speed_label = tk.Label(root, text="Wind speed: ")
wind_direction_label = tk.Label(root, text="Wind direction: ")
humidity_label = tk.Label(root, text="Humidity: ")
pressure_label = tk.Label(root, text="Pressure: ")
# pack
entry.pack()
button.pack()
temperature_label.pack()
wind_speed_label.pack()
wind_direction_label.pack()
humidity_label.pack()
pressure_label.pack()

root.mainloop()
