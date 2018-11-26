from kivy.app import App
from kivy.lang import Builder


kv = '''
BoxLayout:
    orientation: 'vertical'
    Label:
        font_size: 45
        text: 'Yo!  Hi there Desert Py'
        color: .3, .5, .5, 1
    Button:
        font_size: 30
        text: 'You can push this button'
'''
if __name__ == '__main__':
    class Ex1App(App):

        def build(self):
            return Builder.load_string(kv)

    Ex1App().run()
