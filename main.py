# import kivy
#
# import kivy.app

# import kivy.uix.label
from kivy.app import App
from kivy.uix.button import Button

class FristApp(App):
    def build(self):
        btn1 = Button(text="Hola mundo", font_size=30, size_hint=(0.3, 0.2), pos=(250, 250), background_color=("cyan") )
        return btn1
if __name__ =="__main__":
    FristApp().run()
    ññ
