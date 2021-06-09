import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from student_model import Student_model


class Grid(GridLayout):

    def __init__(self, **kwargs):
        super(Grid, self).__init__()

        self.cols = 2

        self.add_widget(Label(text="student name : "))
        self.s_name = TextInput(multiline=False)
        self.add_widget(self.s_name)

        self.add_widget(Label(text="student marks :"))
        self.s_marks = TextInput(multiline=False)
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="student age : "))
        self.s_age = TextInput(multiline=False)
        self.add_widget(self.s_age)

        self.add_widget(Label(text="student attandence :"))
        self.s_at = TextInput(multiline=False)
        self.add_widget(self.s_at)

        self.press = Button(text="click me")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
        self.info_label = Label(text="")
        self.add_widget(self.info_label)

    def click_me(self,instance):
        print(f"your name is \"{self.s_name.text}\" ")
        print(f"your marks is \"{self.s_marks.text}\" ")
        print(f"your age is \"{self.s_age.text}\" ")
        print(f"your age is \"{self.s_at.text}\" ")

        a = Student_model()

        a.add_student_info(self.s_name.text, self.s_marks.text,self.s_age.text,self.s_at.text)

        self.s_name.text = ""
        self.s_marks.text = ""
        self.s_age.text = ""
        self.s_at.text = ""

        self.info_label.text = "your details entered succsessfully"


class SpartanApp(App):

    def build(self):
        return Grid()


if __name__ == "__main__":
    SpartanApp().run()
