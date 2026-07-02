import mysql.connector
from PIL import Image
from io import BytesIO
from kivymd.app import MDApp
from kivy.uix.stencilview import StencilView
from kivymd.
from kivymd.uix.imagelist import imagelist
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import NoTransition , ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.fitimage import FitImage
from kivymd.uix.filemanager import MDFileManager

def fetchData():
    connection = mysql.connector.connect(host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
    cursor = connection.cursor()
    cursor.execute('''select * from userData''')
    print(cursor.fetchone()[3:])
    cursor.fetchall()
    cursor.close()

def scrollableWidget():
    scrollable = MDRecycleView(pos_hint={"center_x":0.5,"center_y":0.5})
    scrollableFrame = MDBoxLayout(orientation="vertical",adaptive_height=True,spacing="10dp",padding="10dp")
    scrollable.add_widget(scrollableFrame)
    return scrollable,scrollableFrame

class tryScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        layout.add_widget(MDRaisedButton(text='Back',on_release=lambda x:setattr(self.manager,"current","login"),pos_hint={'center_x':0.1,'top':0.1}))
        layout.add_widget(StencilView(size_hint=(0.8,0.8),pos_hint={'center_x':0.5,'center_y':0.5}))
        self.add_widget(layout)

class AdminScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        layout.add_widget(MDRaisedButton(text='Fetch',on_release=lambda x:fetchData()))
        layout.add_widget(MDRaisedButton(text='Back',on_release=lambda x:setattr(self.manager,"current","login"),pos_hint={'center_x':0.1,'top':0.1}))
        fileManager = MDFileManager()
        fileManager.show('/storage/emulated/0')
        # scroll , scrollFrame = scrollableWidget()
        # layout.add_widget(scroll)
        self.add_widget(layout)

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        bg = FitImage(source="icons&Images/userbg.png",size_hint=(1,1))
        layout.add_widget(bg)
        layout.add_widget(MDLabel(text="Login Screen",halign="center",pos_hint={"center_x":0.5,"center_y":0.5}))
        btn = MDRaisedButton(text="Back",on_release=lambda x:setattr(self.manager,"current","login"),pos_hint={"center_x":0.5,"center_y":0.1})
        layout.add_widget(btn)
        self.add_widget(layout)

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        bg = FitImage(source="icons&Images/image1.png",size_hint=(1,1))
        layout.add_widget(bg)
        card = MDCard(orientation="vertical",size_hint=(0.3,0.3),pos_hint={"center_x":0.5,"center_y":0.5},md_bg_color=(0,0,0,0.4))
        emailWidget = MDTextField(hint_text="Email",pos_hint={"center_x":0.5,"center_y":0.7},size_hint=(0.8,0.1))
        passwordWidget = MDTextField(hint_text="Password",pos_hint={"center_x":0.5,"center_y":0.5},size_hint=(0.8,0.1),password=True)
        card.add_widget(emailWidget);card.add_widget(passwordWidget)
        card.add_widget(MDRaisedButton(text="Login",on_release=lambda x:setattr(self.manager,"current","home")))
        card.add_widget(MDRaisedButton(text="Admin",on_release=lambda x:setattr(self.manager,"current","admin")))
        layout.add_widget(MDRaisedButton(text='Try',on_release=lambda x:setattr(self.manager,"current","try")))
        layout.add_widget(card)
        self.add_widget(layout)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(AdminScreen(name="admin"))
        sm.add_widget(tryScreen(name="try"))
        return sm

MainApp().run()