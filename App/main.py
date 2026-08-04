import mysql.connector
from PIL import Image
from io import BytesIO
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.stencilview import StencilView
from kivy.animation import Animation
from kivymd.uix.imagelist import imagelist
from kivymd.uix.recycleview import MDRecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
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
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.scrollview import MDScrollView

fieldList = ['Name','Profession','Date of birth','Gender','Qualification','Height','Income','Background','Marital Status','Languages Known',"Father's Name","Mother's Name",
             "Parent's Number",'Whatsapp Number','Family Status','Hometown','Current Resident Address','Siblings','Local Faith Home','Centre Faith Home','Expectations']

def fetchData():
    connection = mysql.connector.connect(host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
    cursor = connection.cursor()
    cursor.execute('''select * from userData''')
    cursor.fetchall()
    cursor.close()

def scrollableWidget():
    scrollable = MDRecycleView(pos_hint={'x':0.5,'y':0.5})
    scrollableFrame = MDBoxLayout(orientation='vertical',adaptive_height=True,spacing='10dp',padding='10dp')
    scrollable.add_widget(scrollableFrame)
    return scrollable,scrollableFrame

def userForm(data=None):
    scrollableFrame = MDScrollView(size_hint=(1, 0.9),pos_hint={'x':0,'y':0})
    layout = MDBoxLayout(orientation='vertical',adaptive_height=True,spacing='10dp',padding='10dp')
    for i in fieldList:layout.add_widget(MDTextField(hint_text=i,helper_text=f'Enter your {i}',size_hint=(0.8,None),pos_hint={'center_x':0.5}))
    scrollableFrame.add_widget(layout)
    return scrollableFrame

class FormScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        layout.add_widget(MDTopAppBar(title='User Form',pos_hint={'top':1},left_action_items=[['arrow-left',lambda x:setattr(self.manager,'current','home')]]))
        layout.add_widget(userForm())
        self.add_widget(layout)
        
class CardItem(RecycleDataViewBehavior,MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, None)
        self.size = (dp(150),dp(150))
        self.md_bg_color = (0, 0, 0, 0.3)

class TryScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        layout.add_widget(MDRaisedButton(text='Back',on_release=lambda x:setattr(self.manager,'current','login'),pos_hint={'center_x':0.1,'top':0.1}))
        scrollableFrame = MDRecycleView();gridScroll = MDRecycleGridLayout(cols=3,spacing=dp(10),padding=dp(10))
        gridScroll.bind(minimum_height=gridScroll.setter('height'))
        scrollableFrame.add_widget(gridScroll)
        scrollableFrame.layout_manager = gridScroll
        scrollableFrame.data = [{"md_bg_color": (0, 0, 0, 0.3)} for _ in range(100)]
        scrollableFrame.viewclass = CardItem
        layout.add_widget(scrollableFrame)
        self.add_widget(layout)

class AdminScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        layout.add_widget(MDRaisedButton(text='Fetch',on_release=lambda x:fetchData()))
        layout.add_widget(MDRaisedButton(text='Back',on_release=lambda x:setattr(self.manager,'current','login'),pos_hint={'center_x':0.1,'top':0.1}))
        fileManager = MDFileManager()
        fileManager.show('/storage/emulated/0')
        self.add_widget(layout)

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        toolbar = MDTopAppBar(title='Pentacostal Matrimony',pos_hint={'top': 1},left_action_items=[['menu',lambda x:print('Menu')]],
                right_action_items=[['magnify',lambda x:print('Search')],['account',lambda x:setattr(self.manager,'current','form')]],)
        layout = MDFloatLayout()
        layout.add_widget(FitImage(source='icons&Images/userbg.png',size_hint=(1,1)));layout.add_widget(toolbar)
        layout.add_widget(MDRaisedButton(text='Back',on_release=lambda x:setattr(self.manager,'current','login'),pos_hint={'center_x':0.5,'center_y':0.1}))
        # scrollableFrame = MDRecycleView();gridScroll = MDRecycleGridLayout(cols=3,spacing=dp(10),padding=dp(10))
        # gridScroll.bind(minimum_height=gridScroll.setter('height'))
        # scrollableFrame.add_widget(gridScroll)
        # scrollableFrame.layout_manager = gridScroll
        # scrollableFrame.data = [{"md_bg_color": (0, 0, 0, 0.3)} for _ in range(100)]
        # scrollableFrame.viewclass = 'MDCard'
        # layout.add_widget(scrollableFrame)
        self.add_widget(layout)

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        bg = FitImage(source='icons&Images/image1.png',size_hint=(1,1))
        layout.add_widget(bg)
        card = MDCard(orientation='vertical',size_hint=(0.4,0.4),pos_hint={'center_x':0.5,'center_y':0.5},md_bg_color=(0,0,0,0.5)
                      ,elevation=4,shadow_radius=6)
        emailWidget = MDTextField(hint_text='Email',helper_text='Enter your email',pos_hint={'x':0.1,'y':0.1},size_hint=(0.8,0.1))
        passwordWidget = MDTextField(hint_text='Password',helper_text='Enter your password',pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.8,0.1),password=True)
        card.add_widget(emailWidget);card.add_widget(passwordWidget)
        card.add_widget(MDRaisedButton(text='Login',on_release=lambda x:setattr(self.manager,'current','home')))
        card.add_widget(MDRaisedButton(text='Admin',on_release=lambda x:setattr(self.manager,'current','admin')))
        layout.add_widget(MDRaisedButton(text='Try',on_release=lambda x:setattr(self.manager,'current','try')))
        layout.add_widget(card)
        self.add_widget(layout)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screenManager = ScreenManager(transition=NoTransition())
        screenManager.add_widget(LoginScreen(name='login'))
        screenManager.add_widget(HomeScreen(name='home'))
        screenManager.add_widget(AdminScreen(name='admin'))
        screenManager.add_widget(TryScreen(name='try'))
        screenManager.add_widget(FormScreen(name='form'))
        return screenManager

MainApp().run()