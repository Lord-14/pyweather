from tkinter import*

def __init__(self, root):
  self.root = root
  self.var_search=StringVar()
  self.root.title("Global Weather App")
  self.root.geometry("400x400")
  name=Label(self.root,text="WeatherApp", font=("agency fb", 18, "underline"))
  city=Label(self.root,text="City", font=("agency fb", 16))
  dataEntry=Entry(self.root, textvariable=self.var_search, font=("agency fb", 12)
  self.root.config(bg="blue")
  
