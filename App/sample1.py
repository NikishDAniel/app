import mysql.connector,threading
from PIL import Image
from io import BytesIO
from kivy.core.image import Image as CoreImage
from kivymd.uix.list import MDList,MDListItem,MDListItemHeadlineText,MDListItemLeadingAvatar
from kivymd.app import MDApp
from kivy.uix.image import Image as KivyImage
from kivymd.uix.fitimage import FitImage
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.floatlayout import MDFloatLayout

class MainScreen(MDApp):
    def build(self):
        layout = MDFloatLayout()
        scroll = MDScrollView()
        list = MDList()
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
        cursor = connection.cursor(dictionary=True)
        cursor.execute('select photo,name from userData')
        result = cursor.fetchall()
        cursor.close();connection.close()
        index = 0
        for i in range(10):
            image = result[i]['photo']
            if image==None:continue
            data = BytesIO(image)
            fmt = Image.open(data).format.lower()
            data.seek(0)
            avatar = MDListItemLeadingAvatar()
            avatar.add_widget(FitImage(texture=CoreImage(data,ext=fmt).texture))
            list.add_widget(MDListItem(avatar,MDListItemHeadlineText(text=result[i]['name'])))
            index += 1
        scroll.add_widget(list)
        layout.add_widget(scroll)
        return layout
            
MainScreen().run()