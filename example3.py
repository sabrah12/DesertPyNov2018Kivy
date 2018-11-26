import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
kivy.require('1.10.1')

Builder.load_string('''
#:kivy 1.10.1
<Ex3>:
    Button:
        id: alice
        text: 'Alice'
        color: 0, 0, 1, 1
        font_size: 50
        size_hint: None,None
        size: 600,600

    Button:
        pos: ( 700, 0 )
        size_hint: None,None
        size: 100,40
        text: 'Drink me'
        color: 1, 0, 0, 1
        font_size: 20
        on_press: alice.size = alice.width-50,alice.height-50
    Button:
        pos: ( 700, 60 )
        size_hint: None,None
        size: 100,40
        text: 'Eat me'
        font_size: 20
        color: 0, 1, 0, 1
        on_press: alice.size = alice.width+50,alice.height+50
''')
class Ex3(FloatLayout):
    pass

class Ex3App(App):
    def build(self):
        r = Ex3()
        print('Ids dictionary in the app are: ',r.ids)
        print("The IDs in the app are:  ",r.ids.keys())
        return r

if __name__ == '__main__':
    Ex3App().run()
