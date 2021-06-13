from guizero import App, MenuBar, PushButton, Text, ListBox
def file_function():
  print("It ain't gonna work.")
def press():
  print("pushing buttons...")
def change_color():
  t.text_color = value
app = App()
menubar = MenuBar(app, Toplevel = ["File", "nothingness"], options=[[["not a thing", file_function]]])

button = PushButton(app, command = press) 

t= Text(app, text="it'sa listbox?!?!", color = "black")
listbox = ListBox(app, items=["red","green","blue"], selected="black",command=change_color)

app.display()
