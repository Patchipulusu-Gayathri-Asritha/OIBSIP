from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import requests

def getWeather(city):
    API_key="6d9a017ca700adbe7848ee20b8bab059"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    result=requests.get(url)

    if result.status_code==404:
        messagebox.showerror("Error","City not Found")
        return None
    try:
        weather=result.json()
        icon_id=weather['weather'][0]['icon']
        temparature=weather['main']['temp']-273.15
        feelslike=weather['main']['feels_like']-273.15
        pressure=weather['main']['pressure']
        humidity=weather['main']['humidity']
        description=weather['weather'][0]['description']
        city=weather['name']
        country=weather['sys']['country']

        icon_url=f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        return (city,country,temparature,feelslike,pressure,humidity,description,icon_url)

    except Exception as e:
        messagebox.showwarning("Information Not Found",f"{e} not Found")

def search():
    city=city_entry.get()
    result=getWeather(city)
    if result is None:
        return

    city,country,temparature,feelslike,pressure,humidity,description,icon_url=result
    
    if country=="IN":
        country="INDIA"
        
    location_label.config(text=f"{city}, {country}")

    image=Image.open(requests.get(icon_url,stream=True).raw)
    icon=ImageTk.PhotoImage(image)
    icon_label.config(bg="#ffd000")
    icon_label.config(image=icon)
    icon_label.image=icon

    temparature_label.config(text=f"Temparature : {temparature:.2f} °C")
    feelslike_label.config(text=f"Feels like {feelslike:.2f} °C")
    pressure_label.config(text=f"Pressure : {pressure} hPa")
    humidity_label.config(text=f"Humidity : {humidity} %")
    description_label.config(text=f"Description : {description}")
    

window=Tk()
window.title("Weather Application")
window.geometry("550x550")
window.config(background="lavender")

searchIcon=PhotoImage(file="C:/Users/pooji/OneDrive/Documents/GlobeSearch.png")

image_label=Label(window,image=searchIcon,bg="lavender")
image_label.pack(pady=5)

city_entry=Entry(window,font=("Goudy Old Style",18),relief=RAISED)
city_entry.pack(pady=10)

search_button=Button(window,text="Search",command=search,bg="#ffd000",relief=RAISED,bd=2,width=10)
search_button.pack(pady=10)

location_label=Label(window,font=("Goudy Old Style",18),bg="lavender")
location_label.pack(pady=10)

icon_label=Label(window,bg="lavender")
icon_label.pack(pady=10)

temparature_label=Label(window,font=("Goudy Old Style",18),bg="lavender")
temparature_label.pack()

feelslike_label=Label(window,font=("Goudy Old Style",18),bg="lavender")
feelslike_label.pack()

pressure_label=Label(window,font=("Goudy Old Style",18),bg="lavender")
pressure_label.pack()

humidity_label=Label(window,font=("Goudy Old Style",18),bg="lavender")
humidity_label.pack()

description_label=Label(window,font=("Goudy Old Style",18),bg="lavender")
description_label.pack()


window.mainloop()
