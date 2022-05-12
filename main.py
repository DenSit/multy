from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from outfunc import solution, helping, solve_time
import random
import time


class Field(Widget):
    """
    field where other widgets are
    """

    factor1 = NumericProperty(random.randint(10, 99))
    factor2 = NumericProperty(random.randint(10, 99))
    count = NumericProperty(0)                          # count of solved problems
    hint = NumericProperty(0)                           # count of used hints
    num = {}                                            # inputted digits
    t = time.time()

    def next(self):
        """
        solve processing and creating a final result table
        """
        answer = self.factor1 * self.factor2
        solve = solution(self.num)
        for i in 'abcdefghij':
            exec(f'self.ids.{i}.text = ""')   # clearing textinput cells
        if answer == solve:
            self.count += 1
            if self.count == 5:
                text = f'Ваш результат: \n\nПримеров решено _______________ {self.count}\nПодсказок использовано ' \
                       f'_______ {self.hint}\nВремя решения _____________ {solve_time(time.time(), self.t)}'
                finish = Finish()
                finish.add_widget(Label(text=text, pos=(340, 350), font_size=30, bold=True,
                                        outline_color='black', outline_width=1))
                self.add_widget(finish)
                self.count = 0
                self.hint = 0
            self.factor1 = random.randint(10, 99)
            self.factor2 = random.randint(10, 99)
            self.t = time.time()
        self.num = {}

    def on_text(self, key, value):
        """
        reading answer from textinput fields
        :param key: textinput sequence number
        :param value: digit
        """
        self.num[key] = value if value else '0'

    def popup(self):
        """
        hints from the multiplication table
        """
        self.hint += 1
        lst = helping(str(self.factor1), str(self.factor2))
        content = BoxLayout(orientation='vertical', padding=15, spacing=30)
        for i in range(4):
            content.add_widget(Label(text=lst[i], font_size='60'))
        but = Button(text='OK', size=(100, 40))
        content.add_widget(but)
        popup = Popup(size_hint=(.85, .85), title='Подсказки из таблицы умножения:',
                      title_align='center', content=content, title_size='25sp')
        but.bind(on_release=popup.dismiss)
        popup.open()

    def change_time(self):
        self.t = time.time()


class Finish(FloatLayout):
    """
    Show the results of exercise
    """
    pass


class MyTextInput(TextInput):
    """
    redefinition the class TextInput to constrain input text with one symbol
    """
    def insert_text(self, substring, from_undo=False):
        if len(self.text) > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)


class MultyApp(App):
    def build(self):
        return Field()


if __name__ == '__main__':
    MultyApp().run()
