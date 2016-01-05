from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from time import sleep

class SelectionScreen(GridLayout):
    def makeGT(self):
        print ("1 part Gin")
        sleep(1)
        print ("3 parts Tonic Water")
        sleep(3)
        print ("All done!")
        return True

    def makeWG(self):
        print ("1 part Whiskey")
        sleep(1)
        print ("3 parts Ginger Ale")
        sleep(3)
        print ("All done!")
        
class DrinkMixer(App):
    def build(self):
        return SelectionScreen()
    
if __name__== "__main__":
    DrinkMixer().run()
