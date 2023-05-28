# main.py
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from sympy import symbols, diff, integrate, pprint, exp, log, sin, cos, tan, rad, ln, pi, E

LabelBase.register(name='CustomFont', fn_regular='D:\sketch_gothic_school\Sketch_Gothic_School.ttf')
LabelBase.register(name='CustomFont2', fn_regular='D:\Deutsch-Gothic\Deutsch.ttf')

Builder.load_string('''
<MainScreen>:
    orientation: 'vertical'
    spacing: '10dp'
    padding: '10dp'
    
    FloatLayout:
        Image:
            source: 'math.jpg'
            allow_stretch: True
            keep_ratio: False
            size_hint: None, None
            size: root.width, root.height

    BoxLayout:
        size_hint_y: None
        height: '50dp'
        pos_hint: {'top': 0.25}
        Label:
            text: 'The Art of Calculus'
            font_name: 'CustomFont'
            font_size: '65sp'
            color: 1, 1, 1, 1 

    GridLayout:
        cols: 2
        rows: 2
        size_hint: 1, None
        height: self.minimum_height
        spacing: '10dp'
        anchor_x: 'center'
        anchor_y: 'center'

        Label:
            text: 'Enter a function'
            font_name: 'CustomFont2'
            font_size: '25sp'
            size_hint_y: None
            height: '48dp'
            color: 0, 0, 0, 1
        TextInput:
            id: input_func
            hint_text: 'f(x)'
            multiline: False
            background_color: 1, 1, 1, 1

        Label:
            text: 'Point (optional)'
            font_name: 'CustomFont2'
            font_size: '25sp'
            size_hint_y: None
            height: '48dp'
            color: 0, 0, 0, 1
        TextInput:
            id: point_input
            hint_text: 'x ='
            multiline: False
            background_color: 1, 1, 1, 1

    BoxLayout:
        size_hint_y: None
        height: '60dp'
        Button:
            text: 'Derive'
            on_press: root.derive_func()
            background_color: 0.5, 0.7, 0.9, 1

    BoxLayout:
        size_hint: 1, None
        height: '60dp'
        Label:
            text: 'Lower limit (optional)'
            font_name: 'CustomFont2'
            font_size: '25sp'
            color: 0, 0, 0, 1
        TextInput:
            id: lower_limit
            hint_text: 'a ='
            multiline: False
            background_color: 1, 1, 1, 1

    BoxLayout:
        size_hint: 1, None
        height: '60dp'
        Label:
            text: 'Upper limit (optional)'
            font_name: 'CustomFont2'
            font_size: '25sp'
            color: 0, 0, 0, 1
        TextInput:
            id: upper_limit
            hint_text: 'b ='
            multiline: False
            background_color: 1, 1, 1, 1

    Button:
        text: 'Integrate'
        on_press: root.integrate_func()
        size_hint_y: None
        height: '60dp'
        background_color: 0.5, 0.7, 0.9, 1

    TextInput:
        id: output_func
        hint_text: 'Result'
        readonly: True
        multiline: True
        height: '200dp'
        background_color: 0.9, 0.9, 0.9, 1

    Button:
        text: 'Reset'
        on_press: root.reset_fields()
        size_hint_y: None
        height: '60dp'
        background_color: 0.9, 0.5, 0.5, 1

''')

class MainScreen(BoxLayout):
    def derive_func(self):
        input_text = self.ids.input_func.text
        if input_text:
            x = symbols('x')
            func = eval(input_text.replace('^', '**').replace('pi', 'pi').replace('e', 'E'))
            point_text = self.ids.point_input.text.strip()
            if point_text:
                point = float(point_text)
                derivative = diff(func, x)
                result = derivative.subs(x, point)
                self.ids.output_func.text = self.format_output(result)
            else:
                derivative = diff(func, x)
                self.ids.output_func.text = self.format_output(derivative)

    def integrate_func(self):
        input_text = self.ids.input_func.text
        if input_text:
            x = symbols('x')
            func = eval(input_text.replace('^', '**').replace('pi', 'pi').replace('e', 'E'))
            lower_limit_text = self.ids.lower_limit.text.strip()
            upper_limit_text = self.ids.upper_limit.text.strip()
            if lower_limit_text and upper_limit_text:
                lower_limit = float(lower_limit_text)
                upper_limit = float(upper_limit_text)
                if 'sin' in input_text or 'cos' in input_text or 'tan' in input_text:
                    lower_limit_radians = rad(lower_limit)
                    upper_limit_radians = rad(upper_limit)
                    definite_integral = integrate(func, (x, lower_limit_radians, upper_limit_radians))
                    self.ids.output_func.text = self.format_output(definite_integral)
                else:
                    definite_integral = integrate(func, (x, lower_limit, upper_limit))
                    self.ids.output_func.text = self.format_output(definite_integral)
            else:
                indefinite_integral = integrate(func, x)
                indefinite_integral += symbols('C')  # Add + C for indefinite integrals
                self.ids.output_func.text = self.format_output(indefinite_integral)

    def format_output(self, result):
        if 'ln' in str(result):
            return str(result).replace('**', '^').replace('pi', 'π').replace('exp(x)', 'e^x').replace('E', 'e')
        else:
            return str(result).replace('**', '^').replace('exp(x)', 'e^x').replace('E', 'e')

    def reset_fields(self):
        self.ids.input_func.text = ''
        self.ids.point_input.text = ''
        self.ids.lower_limit.text = ''
        self.ids.upper_limit.text = ''
        self.ids.output_func.text = ''

class MyApp(App):
    def build(self):
        self.title = 'The Art of Calculus'
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
