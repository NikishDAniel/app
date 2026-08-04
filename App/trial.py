from threading import Thread
import base64,filetype
from mysql.connector import pooling
from nicegui import ui,app,run

connectionPool = pooling.MySQLConnectionPool(pool_name='pool1',pool_size=25,host='127.0.0.1',user='root',password='Nikish@2003',database='pentecostmatrimony')
@ui.page('/home')
def home():
    def loadData():
        connection = connectionPool.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute('select id,photo,name from userData')
            data = cursor.fetchall()
            cursor.close();connection.close()
            with scrollable:
                for i in data:
                    photo = i[1]
                    if photo:ui.image(f"data:image/{filetype.guess(photo).mime or 'jpeg'};base64,{base64.b64encode(photo).decode()}").on('click',lambda e,id=i[0]:ui.notify(f'User ID: {id}'))
        except Exception as e:print(e)
    ui.button('Back',on_click=lambda:ui.navigate.to('/'))
    with ui.card().classes('w-full h-screen items-center justify-center overflow-auto'):scrollable = ui.grid(columns=4).classes('w-full h-full gap-2')
    Thread(target=loadData,daemon=True).start()
    
@ui.page('/')
def main():
    ui.button('Enter',on_click=lambda:ui.navigate.to('/home'))
    
ui.run(host='0.0.0.0',port=8080)