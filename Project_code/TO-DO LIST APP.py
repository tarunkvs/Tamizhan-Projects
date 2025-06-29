import tkinter as tk
from tkinter import messagebox,simpledialog
import json
import os
FILE='tasks.json'
def load():
    if os.path.exists(FILE):
        with open(FILE,'r') as f:
            return json.load(f)
    return []
def save():
    with open(FILE,'w') as f:
        json.dump(task,f)
def refresh():
    listbox.delete(0,tk.END)
    for t in task:
        mark='✔' if t['done'] else '❌'
        listbox.insert(tk.END,f"{mark} {t['task']}")
def add():
    name=simpledialog.askstring("Task","ENTER YOUR TASK=")
    if name:
        task.append({'task': name, 'done': False})
        save()
        refresh()
def edit():
    i=listbox.curselection()
    if i:
        name=simpledialog.askstring("edit task","update task",initialvalue=task[i[0]]['task'])
        if name:
            task[i[0]]['task']=name
            save()
            refresh()
def delete():
    i=listbox.curselection()
    if i:
        task.pop(i[0])
        save()
        refresh()
def complete():
    i=listbox.curselection()
    if i:
        task[i[0]]['done']=True
        save()
        refresh()
app=tk.Tk()
app.title("To-Do App")
app.configure(bg='#990011')
task=load()
listbox=tk.Listbox(app,height=10,width=80,fg="white", font=("Arial", 12), selectbackground="#F7C5CC")
listbox.pack(pady=20)
refresh()
for(txt,cmd) in [('ADD',add),('EDIT',edit),('DELETE',delete),('MARK COMPLETE',complete)]:
    tk.Button(app,text=txt,command=cmd,width=20,bg='#FCF6F5').pack(pady=20)
app.mainloop()
