import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from student_model import person



class person_personal_info(GridLayout):

    def __init__(self, **kwargs):
        super(person_personal_info, self).__init__()

        self.cols = 2

        self.add_widget(Label(text="person name : "))
        self.p_name = TextInput(multiline=False)
        self.add_widget(self.p_name)

        self.add_widget(Label(text="person's mobile number : "))
        self.p_no = TextInput(multiline=False)
        self.add_widget(self.p_no)

        self.add_widget(Label(text="person's age :"))
        self.p_age = TextInput(multiline=False)
        self.add_widget(self.p_age)

        self.add_widget(Label(text="person's graduation :"))
        self.p_graduation = TextInput(multiline=False)
        self.add_widget(self.p_graduation)

        self.press = Button(text="click me")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
        self.info_label = Label(text="")
        self.add_widget(self.info_label)

    def click_me(self, instance):
        print(f"your name is \"{self.p_name.text}\" ")
        print(f"your marks is \"{self.p_no.text}\" ")
        print(f"your age is \"{self.p_age.text}\" ")
        print(f"your age is \"{self.p_graduation.text}\" ")

        x = person()

        x.personal_info(self.p_name.text, self.p_no.text, self.p_age.text, self.p_graduation.text)

        self.p_name.text = ""
        self.p_no.text = ""
        self.p_age.text = ""
        self.p_graduation.text = ""

        self.info_label.text = "your details entered succsessfully"


class Personal_App(App):

    def build(self):
        return person_personal_info()


if __name__ == "__main__":
    Personal_App().run()
