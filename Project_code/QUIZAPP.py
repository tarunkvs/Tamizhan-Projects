import tkinter as tk

# Questions data
questions = [
    {"quest":"Which of the following is the correct extension of the Python file?","options":['.python','.pl','.py','.p'],"ans":'.py'},
    {"quest":"What will be the value of the following Python expression?  print(4 + 3 % 5)","options":[7,2,4,1],"ans":7},
    {"quest":"Which keyword is used for function in Python language?","options":['function','def','Fun','Define'],"ans":'def'},
    {"quest":"What does pip stand for python?","options":["Pip Installs Python","Pip Installs Packages","Preferred Installer Program","All of the mentioned"],"ans":"Preferred Installer Program"},
    {"quest":"Which of the following functions is a built-in function in python?","options":['factorial()','print()','seed()','sqrt()'],"ans":'print()'},
    {"quest":"Which one of the following is not a keyword in Python language?","options":['pass','eval','assert','nonlocal'],"ans":'eval'},
    {"quest":"What arithmetic operators cannot be used with strings in Python?","options":['*','-','+','All of the mentioned'],"ans":'-'},
    {"quest":"Which of the following statements is used to create an empty set in Python?","options":['()','[]','{}','set()'],"ans":'set()'},
    {"quest":"What are the two main types of functions in Python?","options":['System function','Custom function','Built-in function & User defined function'],"ans":'Built-in function & User defined function'},
    {"quest":"Which of the following is a Python tuple?","options":['{1,2,3}','{}','[1,2,3]','(1,2,3)'],"ans":'(1,2,3)'}
]

# Initialize variables
index = 0
user_answers = [None] * len(questions)

# Load current question
def load_question():
    question_label.config(text=questions[index]["quest"])
    var.set(user_answers[index])  # restore selected option if any

    for i in range(4):
        option_buttons[i].config(text=questions[index]["options"][i], value=questions[index]["options"][i])

# Save answer for current question
def save_answer():
    user_answers[index] = var.get()

# Move to next question
def next_question():
    global index
    save_answer()
    if index < len(questions) - 1:
        index += 1
        load_question()
    else:
        show_result()

# Move to previous question
def prev_question():
    global index
    save_answer()
    if index > 0:
        index -= 1
        load_question()

# Calculate and show result
def show_result():
    save_answer()
    score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q["ans"])
    question_label.config(text=f"Quiz Over!\nYour Score: {score}/{len(questions)}")
    
    # Hide buttons after quiz completion
    for btn in option_buttons:
        btn.pack_forget()
    next_button.pack_forget()
    prev_button.pack_forget()

# Tkinter window
app = tk.Tk()
app.title("Python Quiz App")
app.geometry("600x400")
app.config(bg="#962E2A")

question_label = tk.Label(app, text="", font=('Calibre', 14, 'bold'), wraplength=500, justify='left')
question_label.pack(pady=20)

var = tk.StringVar()

option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(app, text="", variable=var, value="", font=('Calibre', 12), wraplength=500, justify='left')
    btn.pack(anchor="w", pady=2)
    option_buttons.append(btn)

# Navigation buttons
nav_frame = tk.Frame(app,bg='#E3867D')
nav_frame.pack(pady=20)

prev_button = tk.Button(nav_frame, text="Previous", command=prev_question, width=10,bg='#FDF6F6')
prev_button.grid(row=0, column=0, padx=10)

next_button = tk.Button(nav_frame, text="Next", command=next_question, width=10,bg='#FDF6F6')
next_button.grid(row=0, column=1, padx=10)

# Load first question
load_question()

app.mainloop()
