from tkinter import*
class WeatherApp:
  def __init__(self, root):
    self.root = root
    self.var_search=StringVar()
    self.root.title("Global Weather App")
    self.root.geometry("600x400+450+100")
    self.root.config(bg="white")
    name=Label(self.root,text="WeatherApp", font=("agency fb", 18, "underline"))
    name.place(x=0,y=0, relwidth=1,height=40)
    city=Label(self.root,text="City:", font=("agency fb", 16), bg="white")
    city.place(x=-100,y=60,relwidth=1, height=30)
    cityEntry=Entry(self.root,textvariable=self.var_search, font=("agency fb", 15), bg="white")
    cityEntry.place(x=230, y=60, relwidth=0.5,height = 30)

    
  
root=Tk() 
obj=WeatherApp(root)
root.mainloop()
