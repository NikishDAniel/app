import mysql.connector
from collections import defaultdict
from io import BytesIO
from PIL import Image
from kivymd.app import MDApp
from kivy.animation import Animation
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.uix.image import Image as KivyImage
from kivy.core.image import Image as CoreImage

cards = defaultdict()

class MDHoverCard(MDCard):
    def on_enter(self,*args):Animation(elevation=8,duration=0.15).start(self)
    def on_leave(self,*args):Animation(elevation=2,duration=0.15).start(self)

class MainApp(MDApp):
    def assignCard(self,i):
        card = MDHoverCard(size_hint=(1, None),height="100dp",elevation=2,on_release=lambda x:print(i))
        card.data = {'Name':''}
        cards[i] = card
        self.content.add_widget(card)
        
    def refreshPage(self,updater):
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
        cursor = connection.cursor(dictionary=True)
        cursor.execute('''select * from userData where role = "user" limit %s offset %s''',(self.limits,self.page*self.limits,))
        result = cursor.fetchall()
        for i in result:
            i=list(i)
            i.pop(1);print(i)
        self.page += 1 if updater else -1
        cursor.close()
        connection.close()
        
    def build(self):
        self.page = 1
        self.limits = 30
        root = MDFloatLayout()
        toolbar = MDTopAppBar(title="User Form",pos_hint={"top": 1},left_action_items=[["arrow-left", lambda x: print("Home")]],)
        scroll = MDScrollView(size_hint=(1, 0.9),pos_hint={"x":0,"y":0},)
        self.content = MDGridLayout(cols=3,adaptive_height=True,spacing="10dp",padding="10dp",)
        for i in range(self.limits):self.assignCard(i)
        print(cards)
        scroll.add_widget(self.content)
        buttonFrame = MDBoxLayout(orientation="horizontal",size_hint=(1, 0.1),pos_hint={"y":0},spacing="20dp",padding="20dp")
        buttonFrame.add_widget(MDFlatButton(text='Previous',on_release=lambda x:self.refreshPage(0)))
        buttonFrame.add_widget(MDFlatButton(text='Next',on_release=lambda x:self.refreshPage(1)))
        root.add_widget(scroll)
        root.add_widget(toolbar)
        root.add_widget(buttonFrame)
        return root

MainApp().run()