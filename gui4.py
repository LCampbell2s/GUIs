from guizero import App, Combo, TextBox
def you_chose(selected_value):
  if selected value == "two?":
    result.value = "what?"
  else:
    result.value = "yes"
app = App()
combo = Combo(app, options=["uno", "two?", "tres"])
result = Text(app)
input_box = TextBox(app, text="typing area", height = 5, multiline = True)
text = Text(app, text="other stuff was already covered")
app.display()
