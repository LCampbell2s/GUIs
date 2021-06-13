from guizero import App, Window, Text, TextBox

app = App(layout="grid")

name_lable = Text(app, text="Name", grid=[0,1], align="left")
name = TextBox(app, grid=[1,1])
def open_window():
  window.show()
  
def close_window():
  window.hide()

app = App(title="Main Window")
window = Window(app, title="Second Window")
window.hide()
text = Text(window, text="this is on a second window", grid=[0,0])

open_button = PushButtton(app, text="Open", command=open_window)
close_button = PushButtton(window, text="close", command=close_window)



app.display()
