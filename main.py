from time import sleep
from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.widget import Widget
from kivy.uix.button import Button


def makeGinTonic():
    print ('1 part Gin')
    sleep(1)
    print ('3 parts Tonic')
    sleep(3)
    print ('Drink is ready')
    return


def makeWhiskeyGinger():
    print ('1 part Whiskey')
    sleep(1)
    print ('3 parts Ginger Ale')
    sleep(3)
    print ('Drink is ready')
    return


def makeWhiskeyTriple():
    print ('1 part Gin')
    sleep(1)
    print ('3 parts Tonic')
    sleep(3)
    print ('Drink is ready')
    return


class SelectScreen(GridLayout):
    def __init__(self, **kwargs):
        super(SelectScreen, self).__init__(**kwargs)
        self.cols = 3
        self.padding = 25
        self.spacing = 25
        self.add_widget(Button(text="Gin & Tonic"))
        self.add_widget(Button(text="Whiskey Ginger"))
        self.add_widget(Button(text="Whiskey Triple"))


class MixerApp(App):
    def build(self):
        return SelectScreen()


if __name__ == "__main__":
    MixerApp().run()
