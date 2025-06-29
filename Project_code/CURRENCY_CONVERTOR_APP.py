import tkinter as tk
from tkinter import ttk

data={
    'USD':{'INR':85.473,'EUR':0.876,'FJD':2.244,'SGD':1.287,'NPR':136.800,'USD':1},
    'INR':{'USD':0.012,'EUR':0.010,'FJD':0.026,'SGD':0.015,'NPR':1.603,'INR':1},
    'EUR':{'INR':97.500,'USD':1.142,'FJD':2.583,'SGD':1.468,'NPR':156.279,'EUR':1},
    'FJD':{'INR':37.82,'USD':0.44,'EUR':0.39,'SGD':0.57,'NPR':60.52,'FJD':1},
    'SGD':{'INR':66.46,'USD':0.78,'EUR':0.68,'NPR':106.34,'FJD':1.76,'SGD':1},
    'NPR':{'INR':0.63,'USD':0.01,'EUR':0.01,'FJD':0.02,'SGD':0.01,'NPR':0.01},
    'GBP': {'INR': 109.35, 'USD': 1.275, 'EUR': 1.123, 'FJD': 2.942, 'SGD': 1.727, 'NPR': 170.63, 'GBP': 1, 'AUD': 1.837},
    'AUD': {'INR': 59.45, 'USD': 0.687, 'EUR': 0.624, 'FJD': 1.144, 'SGD': 0.893, 'NPR': 92.88, 'GBP': 0.544, 'AUD': 1}
}
def convertor():
    try:
        amount=float(amount_var.get())
        source=source_var.get()
        target=target_var.get()
        if source==target:
            result.set(f"Coverted Amount=> {amount:.2f} {target}")
        else:
            rate=data.get(source,{}).get(target)
            if rate:
                amount_output=rate*amount
                result.set(f"Converted Amount=> {amount_output:.2f} {target}")
            else:
                result.set("Not Available")
    except ValueError:
        result.set("Invalid")
app=tk.Tk()
app.title('Currency Convertor App')
app.geometry('400x400')
app.config(padx=20,pady=20,bg="#7A2048")

amount_var=tk.StringVar()
source_var=tk.StringVar()
target_var=tk.StringVar()
result=tk.StringVar()
currencies=['USD','INR','EUR','FJD','SGD','NPR','GBP','AUD']

tk.Label(app,text='Amount:',font=('calibre',10,'bold')).pack(pady=5)
tk.Entry(app,textvariable=amount_var,font=('calibre',10,'bold')).pack(pady=5)
tk.Label(app,text='From Currency',font=('calibre',10,'bold')).pack(pady=10)
ttk.Combobox(app,textvariable=source_var,values=currencies,state='readonly').pack(pady=10)
tk.Label(app,text='To Currency',font=('calibre',10,'bold')).pack(pady=10)
ttk.Combobox(app,textvariable=target_var,values=currencies,state='readonly').pack(pady=10)
tk.Button(app,text='Convert',command=convertor,font=('calibre',10,'bold')).pack(pady=15)
tk.Label(app,textvariable=result,font=('calibre',10,'bold')).pack(pady=15)
app.mainloop() 



