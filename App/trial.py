from threading import Thread
import base64,filetype
from mysql.connector import pooling
from nicegui import ui,app,run

connectionPool = pooling.MySQLConnectionPool(pool_name='pool1',pool_size=5,host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
page = 0
pageLimit = 20
@ui.page('/home')
def home():
    def loadData(updater=1):
        global page
        connection = connectionPool.get_connection()
        try:
            cursor = connection.cursor()
            if updater:
                cursor.execute("select id from userData where role='user' limit %s offset %s",(pageLimit+1,(page+1)*pageLimit,))
                nextData = cursor.fetchall()
                if len(nextData)>pageLimit:nextButton.enable()
                else:nextButton.disable()
                page += 1
                previous.enable()
            else:
                page -= 1
                if page>0:previous.enable()
                else:previous.disable();page=0
                nextButton.enable()
            offset = page*pageLimit
            cursor.execute("SELECT id, photo, name FROM userData where role='user' limit %s offset %s",(pageLimit,offset,))
            data = cursor.fetchall()
            ui.timer(0,lambda: display_data(data),once=True)
        except Exception as e:print(e)
        finally:cursor.close();connection.close()
    def display_data(data):
        scrollable.clear()
        with scrollable:
            for user_id,photo,name in data:
                if photo:
                    ui.image(f"data:image/{filetype.guess(photo).mime or'jpeg'};base64,{base64.b64encode(photo).decode()}").on("click",lambda e,uid=user_id:ui.notify(f"User ID: {uid}"))
    ui.button('Back',on_click=lambda:ui.navigate.to('/'))
    with ui.card().classes('w-full h-screen items-center justify-center overflow-auto'):scrollable = ui.grid(columns=4).classes('w-full h-full gap-2')
    nextButton = ui.button('Next',on_click=lambda:loadData())
    previous = ui.button('Previous',on_click=lambda:loadData(0))
    loadData(0)
    
@ui.page('/')
def main():
    ui.button('Enter',on_click=lambda:ui.navigate.to('/home'))

ui.run(host='0.0.0.0',port=8080)