from tkinter import* #for build up this app
import requests
import time
from PIL import ImageTk,Image #for image

#function

def getWeather(root):
    city = textField.get()
   #collect weather data
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
   # variables to store data
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    
    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

#main program
    
root=Tk()
root.geometry("700x600")
root.title("Weather App")
root.iconbitmap("C:/Users/HP/Documents/png-transparent-computer-icons-wind-weather-symbol-logo-cloudy-weather-forecasting-black-business.png")
img=Image.open("C:/Users/HP/Documents/3127236.png")
resized_img=img.resize((150,150))
img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(padx=(10,500),pady=(10,10))
f=("arial",15,"bold")
t=("arial",35,"bold")
textField=Entry(root,justify="center",width=15,font=t,bg="grey",fg="light grey")
textField.pack(pady=15)
textField.focus()
textField.bind('<Return>',getWeather)
label1=Label(root,font=t)
label1.pack()
label2=Label(font=f)
label2.pack()

root.mainloop()


