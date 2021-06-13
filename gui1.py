from guizero import App, Text, PushButton, Slider
def say_hello():
  text.value="hello world"

app = App(title="Hello World!")
message = Text(app, text= "Welcome to the Hello World! app.")
button = PushButton(app, command=say_hello)

app.display()
