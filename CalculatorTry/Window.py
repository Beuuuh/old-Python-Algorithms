import tkinter as tk

#Window properties
Window = tk.Tk()
Window.title('Calculadora mt massa')
Window.geometry("300x300")

#Buttons in a list
Buttons = [
'1', '2', '3',
'4', '5', '6',
'7', '8', '9',
'0', '=', 'C',
'+', '-', '*', '/'
]

#Setting the GUI
row = 1
col = 0

#Making the click event and the interaction with the buttons

for i in Buttons:
    button_style = 'raised'
    Event = lambda x = i: click_event(x)
    tk.Button(Window, text = i, width = 7, height = 7, relief = button_style, command = Event) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1
display = tk.Entry(Window, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)

def click_event(key):
    if(key == '='):
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "   Error, use only valid chars")
    elif key == 'C':
        display.delete(0, tk.END)

#Runtime
Window.mainloop()
