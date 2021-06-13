from guizero import App, Text, Box, PushButton, ButtonGroup, CheckBox
def nothing():
  return 0 

app = App(title="My App", height = 300 width = 300 layout = "grid")
text = Text(app, text= "some text", grid [0,0])
box = Box(app, layout = "grid", grid = [1,0])

button1 = Pushbutton(box, command=nothing, text="1", grid[0,0])
button2 = Pushbutton(box, command=nothing, text="2", grid[1,0])

choice = ButtonGroup(app, options=["Ham", "Cheese", "Potato"], selected="cheese", grid[0,1])

checkbox = CheckBox(app, text="explode", grid[0,2])
if checkbox.value == 1:
  app.hide()
app.display()
