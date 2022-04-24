from kivy.config import Config
Config.set('graphics','resizable',1)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('main.kv')

class CalculatorLayout(Widget):
    # function to clear all text box
    def clear(self):
        self.ids.textinput.text = "0"

    # leave 2 numbers after the dot
    def round_res(self,result):
        if "." in list(result):
            result = result.split(".")
            if len(result[1]) > 4:
                result[1] = result[1][0:3]
            return result[0]+"."+result[1]
        return result

    # count the result
    def get_result(self):
        ti = self.ids.textinput.text
        try:
            result = eval(ti)
            result = self.round_res(str(result))
            self.ids.textinput.text = str(result)
        except Exception:
            self.ids.textinput.text = "Error"
        
    # adding numbers to text box
    def button_press(self,button):
        ti = self.ids.textinput.text
        if ti == "0" or ti == "Error":
            self.ids.textinput.text = ""
            self.ids.textinput.text = button
        else:
            self.ids.textinput.text += button

    def add_operator(self,op):
        ti = self.ids.textinput.text
        if len(ti) > 0:
            if not ti[len(ti)-1] in ["+","-","*","/","//"] and ti not in ["0","Error"]:
                self.ids.textinput.text = f"{ti}{op}"
    # backspace funtion
    def remove(self):
        ti = self.ids.textinput.text
        if ti not in ["0","Error"]:
            self.ids.textinput.text = self.ids.textinput.text[0:-1]
    # make negative or positive number
    def neg_pos(self):
        ti = self.ids.textinput.text
        if len(ti) > 0 and ti not in ["0","Error"]:
            if ti[0] == "-":
                self.ids.textinput.text = ti[1:]
            else:
                self.ids.textinput.text = f'-{ti}'


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()
