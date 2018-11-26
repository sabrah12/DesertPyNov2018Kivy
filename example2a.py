from kivy.app import App
from kivy.lang import Builder


kv = '''
BoxLayout:
    orientation: 'vertical'
    width: 300
    size_hint_x: None
    Label:
        text: 'I am a keypad!'
        font_size: 40
        color: 0, 1, 1, 1
    GridLayout:
        width: 300
        size_hint_x: None
        cols: 3
        Button:
            text: '1'
        Button:
            text: '2'
        Button:
            text: '3'
        Button:
            text: '4'
        Button:
            text: '5'
        Button:
            text: '6'
        Button:
            text: '7'
        Button:
            text: '8'
        Button:
            text: '9'
    Label:
        text: 'Dial me!'
        color: 1, 0, 1, 1
        font_size: 50
'''
if __name__ == '__main__':
    class Ex2aApp(App):

        def build(self):
            return Builder.load_string(kv )

    Ex2aApp().run()
