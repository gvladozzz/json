import tkinter as tk
import json
import requests

def get_weather():
    dict = {}
    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop/format/json")
    if response.status_code == 200:
        data = json.loads(response.content)
        for i in range(len(data)):
            dict[data[i]['stacja']] = float(data[i]['temperatura'])
    label.config(text = dict[entry.get()])

root = tk.Tk()
root.geometry("400x400")
root.title("Weather")
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text = "show temperature", command=get_weather)
button.pack()
label = tk.Label(root, text = "0")
label.pack()
root.mainloop()
