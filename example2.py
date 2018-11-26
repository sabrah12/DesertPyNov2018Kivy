from kivy.app import App
from kivy.lang import Builder


kv = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'Drink me'
    Button:
        text: 'Eat me'
    BoxLayout:
        Button:
            text: 'See me'
        Button:
            text: 'Feel me'
        Button:
            text: 'Touch me'
        Button:
            text: 'Heal me'
    Label:
        text: 'Books and Music'
'''
if __name__ == '__main__':
    class Ex1App(App):

        def build(self):
            return Builder.load_string(kv )

    Ex1App().run()
