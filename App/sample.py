from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import NoTransition , ScreenManager
from kivymd.uix.card import MDCard
from kivy.uix.stencilview import StencilView
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        card = MDCard(size_hint=(0.5,0.5),pos_hint={"center_x":0.5,"center_y":0.5},orientation="vertical"
        ,padding="10dp",spacing="10dp",md_bg_color=(0,0,0,0.4),elevation=4,shadow_radius=6)
        card.add_widget(MDRaisedButton(text='Dark Mode',on_release=lambda x:setattr(self.theme_cls,"theme_style","Dark" if self.theme_cls.theme_style=="Light" else "Light")))
        layout.add_widget(card)
        self.add_widget(layout)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(LoginScreen(name="login"))
        return sm

MainApp().run()