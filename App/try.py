import mysql.connector
from io import BytesIO
from PIL import Image
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.uix.image import Image as KivyImage
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.core.image import Image as CoreImage

class CardItem(RecycleDataViewBehavior, MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = dp(8)
        self.spacing = dp(5)
        self.radius = [15]
        self.elevation = 4
        self.img = KivyImage(size_hint=(1,1),allow_stretch=True)
        self.name_lbl = MDLabel(halign="center",adaptive_height=True)
        self.add_widget(self.img)
        self.add_widget(self.name_lbl)
    def refresh_view_attrs(self,rv,index,data):
        self.data = data
        self.name_lbl.text = data["Name"]
        stream = BytesIO(data["Photo"])
        fmt = Image.open(stream).format.lower()
        stream.seek(0)
        self.img = CoreImage(stream,ext=fmt).texture
        return super().refresh_view_attrs(rv,index,data)
    def on_release(self):
        dialog = MDDialog(title=self.data["Name"],text=f"Profession : {self.data['Profession']}")
        dialog.open()

class MainApp(MDApp):
    def build(self):
        layout = MDFloatLayout()
        layout.add_widget(MDTopAppBar(title='User Form',pos_hint={'top':1},left_action_items=[['arrow-left',lambda x:print('home')]]))
        rv = MDRecycleView(size_hint=(1,0.88),pos_hint={'x':0,'y':0})
        grid = MDRecycleGridLayout(cols=3,default_size=(None, dp(180)),default_size_hint=(1, None),size_hint_y=None,spacing=dp(10),padding=dp(10),)
        grid.bind(minimum_height=grid.setter("height"))
        rv.add_widget(grid)
        rv.layout_manager = grid
        rv.viewclass = CardItem
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
        cursor = connection.cursor(dictionary=True)
        cursor.execute('''select * from userData where role = "user"''')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        rv.data = [i for i in result]
        layout.add_widget(rv)
        return layout
MainApp().run()