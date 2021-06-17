from tkinter import*
import aKey
import PIL
from PIL import ImageTk
from PIL import Image
import requests
class WeatherApp:
  def __init__(self, root):
    self.root = root
    self.var_search=StringVar() #Location search
    self.root.title("Global Weather App")
    self.root.geometry("350x400+450+100")
    self.root.config(bg="blue")
    #GUI - Images
    self.img = Image.open("searchicon.jpg")
    self.img = self.img.resize((30,30), Image.ANTIALIAS)
    self.img = ImageTk.PhotoImage(self.img)
    #GUI - NAME, LOCATION, SEARCHBAR, BUTTON
    name=Label(self.root,text="WeatherApp", font=("agency fb", 30, "underline"), bg = "grey")
    name.place(x=0,y=0, relwidth=1,height=60)
    city=Label(self.root,text="Location:", font=("Helvetica bold", 16), bg="maroon4", anchor = "w")
    city.place(x=0,y=60,relwidth=1, height=50)
    cityEntry=Entry(self.root,textvariable=self.var_search, font=("Helvetica", 18), bg="white",  fg="green")
    cityEntry.place(x=100, y=60, width=150,height = 50)
    entryButton=Button(self.root, image=self.img,textvariable=self.var_search, bd=0)
    entryButton.place(x=265, y=63, width=75,height = 45)

    #GUI - Result Data
   # temperature
   # weather
   # location
  

  def getData(self):
    api_key= aKey.apiKey
    url= f"https://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
    r=requests.get(url)
    if r:
      json=r.json()
      locationName=json["name"]
      country=json["sys"]["country"]
      temp=json["main"]["temp"]-273.15 * 9/5 +32
      feelsLike=json["main"]["feels_like"]-273.15 * 9/5 +32
      weather=json["weather"]["description"]


    
  
root=Tk() 
obj=WeatherApp(root)
root.resizable(False, False)
root.mainloop()
