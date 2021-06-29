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
    self.root.config(bg="grey")
    #GUI - Images
    self.img = Image.open("searchicon.jpg")
    self.img = self.img.resize((30,30), Image.ANTIALIAS)
    self.img = ImageTk.PhotoImage(self.img)
    #GUI - NAME, LOCATION, SEARCHBAR, BUTTON
    name=Label(self.root,text="WeatherApp", font=("agency fb", 30, "underline"), bg = "palegreen")
    name.place(x=0,y=0, relwidth=1,height=65)
    city=Label(self.root,text="Location:", font=("Helvetica bold", 16), bg="pale green", anchor = "w")
    city.place(x=0,y=60,relwidth=1, height=50)
    cityEntry=Entry(self.root,textvariable=self.var_search, font=("Helvetica", 18), bg="white",  fg="green")
    cityEntry.place(x=100, y=60, width=190,height = 50)
    entryButton=Button(self.root, image=self.img, bd=0, bg="green", command=self.getData)
    entryButton.place(x=290, y=60, width=60,height = 50)
    bar=Label(self.root, bg="black", anchor = "w").place(x=0,y=110, relwidth=1,height=10)
    #GUI - Result Data
   # temperature
    self.tlbl=Label(self.root,text="Temperature(F)", font=("Helvetica bold", 16), bg="grey", anchor = "w")
    self.tlbl.place(x=0,y=160, relwidth=1,height=20)
   # weather
    self.weatherlbl=Label(self.root,text="Weather", font=("Helvetica bold", 16), bg="grey", anchor = "w")
    self.weatherlbl.place(x=0,y=210, relwidth=1,height=20)
   # location
    self.citylbl=Label(self.root,text="Location", font=("Helvetica bold", 16), bg="grey", anchor = "w")
    self.citylbl.place(x=0,y=260, relwidth=1,height=20)

    
   
  

  def getData(self):
   
    api_key= aKey.apiKey
    url= f"https://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
    if (self.var_search.get()!=""):
      r=requests.get(url)
      if r:
        jsonText=r.json()
        print(self.var_search)
        locationName=jsonText["name"]
        country=jsonText["sys"]["country"]
        temp=(jsonText["main"]["temp"]-273.15) * 9/5 +32
        weather=jsonText["weather"][0]["description"]
        self.tlbl.config(text=str(round(temp)))
        self.weatherlbl.config(text=(weather))
        self.citylbl.config(text=locationName+","+country) 
        print(locationName)
        


    
  
root=Tk() 
obj=WeatherApp(root)
root.resizable(False, False)
root.mainloop()
