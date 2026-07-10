# import mysql.connector
# from threading import Thread
# from PIL import Image
# from io import BytesIO
# from kivymd.app import MDApp
# from kivymd.uix.gridlayout import MDGridLayout
# from kivymd.uix.fitimage import FitImage
# from kivy.core.image import Image as CoreImage
# from kivy.uix.image import Image as KivyImage
# from kivy.graphics.texture import Texture
# from kivymd.uix.scrollview import MDScrollView
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.toolbar import MDTopAppBar
# from kivymd.uix.card import MDCard
# from kivymd.uix.recycleview import MDRecycleView
# from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
# from kivy.animation import Animation
# from kivymd.uix.button import MDRaisedButton
# from kivy.uix.screenmanager import NoTransition , ScreenManager
# from kivymd.uix.card import MDCard
# from kivy.uix.stencilview import StencilView
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.floatlayout import MDFloatLayout

# def loadPhotos(layout,image):
#     data = BytesIO(image)
#     pil = Image.open(data)
#     exten = pil.format.lower();data.seek(0)
#     coreImage = CoreImage(data,ext=exten)
#     layout.add_widget(KivyImage(texture=coreImage.texture))

# class TryScreen(MDScreen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         layout = MDFloatLayout()
#         connection = mysql.connector.connect(host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
#         cursor = connection.cursor()
#         cursor.execute('''select photo from userData where role = "user"''')
#         result = cursor.fetchall()
#         cursor.close();connection.close()
#         # for i in result:Thread(target=loadPhotos, args=(layout, i[0])).start()
#         self.add_widget(layout)

# class MainScreen(MDScreen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         layout = MDRecycleGridLayout(cols=3,spacing="10dp",adaptive_height=True,pos_hint={"x":0.1,"y":0.1})
#         self.add_widget(layout)

# class LoginScreen(MDScreen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         layout = MDFloatLayout()
#         card = MDCard(size_hint=(0.5,0.5),pos_hint={"center_x":0.5,"center_y":0.5},orientation="vertical"
#         ,padding="10dp",spacing="10dp",md_bg_color=(0,0,0,0.4),elevation=4,shadow_radius=6)
#         card.add_widget(MDRaisedButton(text='Dark Mode',on_release=lambda x:setattr(self.theme_cls,"theme_style","Dark" if self.theme_cls.theme_style=="Light" else "Light")))
#         card.add_widget(MDRaisedButton(text='Login',on_release=lambda x:setattr(self.manager,"current","main")))
#         card.add_widget(MDRaisedButton(text='Try',on_release=lambda x:setattr(self.manager,"current","try")))
#         layout.add_widget(card)
#         self.add_widget(layout)

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Light"
#         sm = ScreenManager(transition=NoTransition())
#         sm.add_widget(LoginScreen(name="login"))
#         sm.add_widget(MainScreen(name='main'))
#         sm.add_widget(TryScreen(name='try'))
#         return sm

# MainApp().run()

from kivymd.icon_definitions import md_icons
print(list(filter(lambda x:x.startswith('b'),md_icons.keys())))