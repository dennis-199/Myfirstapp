import kivy
import mysql.connector as sql
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childapp(GridLayout):
    def __init__(self,**kwargs):
        super(childapp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text="Student ID"))
        self.idstudent = TextInput()
        self.add_widget(self.idstudent)

        self.add_widget(Label(text = "Your Names"))
        self.y_name = TextInput()
        self.add_widget(self.y_name)

        self.add_widget(Label(text="Student Marks"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = "click Me")
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)



    def click_me(self, instance):
        id=self.idstudent.text
        yn=self.y_name.text
        sm=self.s_marks.text
        sg=self.s_gender.text
        con=sql.connect(host="localhost",user="root",password="",database = "student")
        cur=con.cursor()
        query = "INSERT INTO students(idstudent,y_name,s_marks,s_gender)VALUES(%s,%s,%s,%s)"
        val=(id,yn,sm,sg)
        cur.execute(query,val)
        con.commit()
        con.close()



class MobileApp(App):
    def build(self):
        return childapp()


if __name__ == "__main__":
    MobileApp().run()

