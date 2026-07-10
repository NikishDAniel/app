import mysql.connector
from collections import defaultdict
from io import BytesIO
from PIL import Image
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.appbar import MDTopAppBar,MDActionTopAppBarButton,MDTopAppBarTitle,MDTopAppBarTrailingButtonContainer,MDTopAppBarLeadingButtonContainer
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDModalDatePicker,MDDockedDatePicker,MDModalInputDatePicker
from kivymd.uix.loadingindicator import MDLoadingIndicator
from kivymd.uix.list import MDList,MDListItem,MDListItemHeadlineText
from kivymd.uix.textfield import MDTextField,MDTextFieldHelperText,MDTextFieldTrailingIcon,MDTextFieldHintText,MDTextFieldLeadingIcon
from kivymd.uix.fitimage import FitImage
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDButton,MDButtonText,MDIconButton,MDButtonIcon
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.metrics import dp
from kivy.uix.image import Image as KivyImage
from kivy.core.image import Image as CoreImage
from kivy.uix.screenmanager import NoTransition,ScreenManager

cards = defaultdict()
fieldList = ['Name','Profession','Date of birth','Gender','Qualification','Height','Income','Background','Marital Status','Languages Known',"Father's Name","Mother's Name",
             "Parent's Number",'Whatsapp Number','Family Status','Hometown','Current Resident Address','Siblings','Local Faith Home','Centre Faith Home','Expectations']
# print(md_icons.keys())

def userForm():
    scroll = MDScrollView(size_hint=(1, 0.9),pos_hint={'x':0,'y':0})
    layout = MDBoxLayout(orientation='vertical',adaptive_height=True,spacing='10dp',padding='10dp')
    for i in fieldList:layout.add_widget(MDTextField(MDTextFieldHintText(text=i),MDTextFieldHelperText(text=f'Enter Your {i}')))
    scroll.add_widget(layout)
    return scroll

class FormScreen(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        root = MDFloatLayout()
        root.add_widget(MDTopAppBar(MDTopAppBarLeadingButtonContainer(MDActionTopAppBarButton(icon='arrow-left-circle',on_release=lambda x:
            setattr(self.manager,'current','login'))),
            MDTopAppBarTitle(text='Registration Form',halign='center'),type='small',pos_hint={'top':1},))
        root.add_widget(userForm())
        self.add_widget(root)

class AdminScreen(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        root = MDFloatLayout()
        root.add_widget(MDButton(MDButtonText(text='Back'),on_release=lambda x:setattr(self.manager,'current','login')))
        self.add_widget(root)

class HomeScreen(MDScreen):
    def assignCard(self,i):
        card = MDCard(size_hint=(1,None),height='100dp',elevation=2,on_release=lambda x:print(i))
        card.data = {'Name':'','':''}
        cards[i] = card
        self.layout.add_widget(card)
    def refreshPage(self,updater):
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
        cursor = connection.cursor(dictionary=True)
        cursor.execute('''select * from userData where role = "user" limit %s offset %s''',(self.limits,self.page*self.limits,))
        result = cursor.fetchall()
        for i in result:
            i.pop('Photo');print(i)
        self.page += 1 if updater else -1
        cursor.close()
        connection.close()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.page = 1
        self.limits = 30
        root = MDFloatLayout()
        root.add_widget(FitImage(source='icons&Images/userbg.png',size_hint=(1,1)))
        root.add_widget(MDTopAppBar(MDTopAppBarLeadingButtonContainer(MDActionTopAppBarButton(icon='logout',on_release=lambda x:setattr(self.manager,'current','login'))),
            MDTopAppBarTitle(text='User Profiles',halign='center'),MDTopAppBarTrailingButtonContainer(
                MDActionTopAppBarButton(icon='account-circle-outline',on_release=lambda x:setattr(self.manager,'current','form')),
                MDActionTopAppBarButton(icon='menu',on_release=lambda x:print('Menu'))),
            type='small',pos_hint={'top':1},))
        scroll = MDScrollView(pos_hint={'top':0.89},size_hint=(1,0.89))
        self.layout = MDGridLayout(cols=3,adaptive_height=True,size_hint=(1,None),spacing='10dp',padding='10dp')
        for i in range(self.limits):self.assignCard(i)
        scroll.add_widget(self.layout)
        root.add_widget(scroll)
        root.add_widget(MDButton(MDButtonText(text='Previous')))
        root.add_widget(MDButton(MDButtonText(text='Next')))
        self.add_widget(root)

class LoginScreen(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        layout.add_widget(FitImage(source='icons&Images/image1.png',size_hint=(1,1)))
        loginCard = MDCard(orientation='vertical',adaptive_height=True,width=dp(400),style="filled",md_bg_color=(0.1,0.1,0.1,0.5),size_hint=(None,None),pos_hint={'center_x':0.5,'center_y':0.5},spacing=dp(20),padding=dp(20))
        email = MDTextField(MDTextFieldLeadingIcon(icon='email'),MDTextFieldHelperText(text='Enter Your Email'),MDTextFieldHintText(text='Email'))
        loginCard.add_widget(email)
        password = MDTextField(MDTextFieldLeadingIcon(icon='lock'),MDTextFieldHelperText(text='Enter Your Password'),MDTextFieldHintText(text='Password'),password=True)
        loginCard.add_widget(password)
        subLayout = MDBoxLayout(orientation='horizontal',adaptive_height=True,spacing=dp(10))
        subLayout.add_widget(MDButton(MDButtonIcon(icon='account-edit'),MDButtonText(text='Register'),on_release=lambda x:setattr(self.manager,'current','form')))
        subLayout.add_widget(MDButton(MDButtonIcon(icon='login'),MDButtonText(text='Login'),on_release=lambda x:setattr(self.manager,'current','home')))
        loginCard.add_widget(subLayout);layout.add_widget(loginCard)
        self.add_widget(layout)
        
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screenManager = ScreenManager(transition=NoTransition())
        screenManager.add_widget(LoginScreen(name='login'))
        screenManager.add_widget(HomeScreen(name='home'))
        screenManager.add_widget(AdminScreen(name='admin'))
        screenManager.add_widget(FormScreen(name='form'))
        return screenManager

MainApp().run()