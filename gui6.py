from guizero import App, Slider, TextBox, Picture
def slider_changed(slider_value):
  textbox.value = slider_value
app = App()
slider=Slider(app, command=slider_changed)
textbox=TextBox(app)

pic=Picture(app,image="images/alien.png")

app.display()
