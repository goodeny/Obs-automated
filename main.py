import os
os.system('pip install beautifulsoup4')
os.system('pip install requests')
from tkinter import *
from bs4 import BeautifulSoup
from GUI import center
import requests
import time
import threading
import json

# ~ goodeny ~

class Software():
    def __init__(self):
        self.create_db_json()
        self.create_note()
        self.window = Tk()
        #usefull variables
        self.news_quantity = self.read_json()['quantity_news']
        self.message = "mensagem personalizada"
        self.name_window = f"{self.get_name_window()}"

        #window settings
        center(self.window, 500, 500)
        self.window.title(f'{self.name_window}')
        self.window.resizable(0,0)
        #background color
        self.BG_COLOR = "#181818"
        self.window.config(bg=self.BG_COLOR)
        #components
        self.logo_name()
        self.settings()
        self.start_button()
        self.log_error('Ready to run!', 0) 

    def start_button(self):
        self.image_start_btn = PhotoImage(file='assets/btn_start.png')
        self.start_btn = Button(self.window, image=self.image_start_btn, cursor="hand2",bd=0, bg=self.BG_COLOR, activebackground=self.BG_COLOR, 
                                command=lambda: threading.Thread(target=self.insert_note).start())
        self.start_btn.place(x=170, y=230)

    def settings(self):
        self.settings_image = PhotoImage(file='assets/btn_config.png')
        self.config_button = Button(self.window, image=self.settings_image, bg=self.BG_COLOR, bd=0, cursor="hand2", activebackground=self.BG_COLOR, command=lambda:self.settings_window())
        self.config_button.place(x=430, y=35)
        
    def log_error(self, message, error):
        self.log_label = Label(self.window, text='', fg="#37FF33", bg=self.BG_COLOR, font='16')
        self.log_label.place(x=20,y=449)
        if error == 1:
            self.log_label.config(fg='#FF3333', text=message)
            self.log_label.update()
        else:
            self.log_label.config(fg='#37FF33', text=message)
            self.log_label.update()

    def create_db_json(self):
        try:
            with open('data.json', 'x') as f:
                pass
            structure = {
                "window_name": "",
                "message": "Custom message",
                "quantity_news": 3
            }
            
            with open('data.json', 'w') as file_w:
                    json.dump(structure, file_w, indent=4)
        except:
            pass

    def running_button(self):
        self.image_running_buttom = PhotoImage(file='assets/btn_running.png')
        self.running_btn = Button(self.window, image=self.image_running_buttom, cursor="hand2",bg=self.BG_COLOR, activebackground=self.BG_COLOR, bd=0)
        self.running_btn.place(x=170, y=230)
    
    def logo_name(self):
        self.label_title = Label(self.window, text=self.name_window, font='16', bg=self.BG_COLOR, fg="white")
        self.label_title.place(x=30, y=45)

    def settings_window(self):
        self.window_settings = Toplevel()
        center(self.window_settings, 500, 380)
        self.window_settings.resizable(0,0)
        self.window_settings.config(bg=self.BG_COLOR)

        #news quantity
        self.label_quantity = Label(self.window_settings, text="News Quantity", font="16", bg=self.BG_COLOR, fg='white')
        self.label_quantity.place(x=35, y=70)

        self.Entry_quantity = Entry(self.window_settings, font="16")
        self.Entry_quantity.place(x=35, y=100, height=35, width=140)
        self.Entry_quantity.insert(0, self.news_quantity)

        #window name
        self.label_window_name = Label(self.window_settings, text="Window Name", font="16", bg=self.BG_COLOR, fg='white')
        self.label_window_name.place(x=35, y=150)

        self.Window_name = Entry(self.window_settings, font="16")
        self.Window_name.place(x=35, y=180, height=35, width=140)

        self.save_name_button = PhotoImage(file="assets/btn_save_name.png")
        self.button_window_name = Button(self.window_settings, image=self.save_name_button, bd=0, activebackground=self.BG_COLOR, bg=self.BG_COLOR, command=lambda:self.change_name_window())
        self.button_window_name.place(x=30, y=230)

        #message
        self.label_message = Label(self.window_settings, text="Message", font="16", bg=self.BG_COLOR, fg='white')
        self.label_message.place(x=220, y=70)

        self.text_message = Text(self.window_settings, font="16")
        self.text_message.place(x=220, y=100, width=250, height=180)
        self.text_message.insert("1.0",self.read_json()['message'])

        self.save_button_img = PhotoImage(file="assets/btn_save.png")
        self.save_button = Button(self.window_settings, image=self.save_button_img, bd=0, activebackground=self.BG_COLOR, bg=self.BG_COLOR, command=lambda: self.save())
        self.save_button.place(x=320, y=320)

        self.window_settings.mainloop()

    def read_json(self):
        with open("data.json", "r") as f:
            data = json.load(f)
        return data

    def insert_message_json(self, message):
        data = self.read_json()
        
        data['message'] = message
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    def insert_name_window(self, name):
        data = self.read_json()
        
        data['window_name'] = name
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def insert_quantity_news_json(self, qnt):
        data = self.read_json()
        
        data['quantity_news'] = qnt
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
            
    def save(self):
        self.message = self.text_message.get('1.0', "end-1c")
        self.insert_message_json(self.message)
        try:
            self.news_quantity = int(self.Entry_quantity.get())
            self.insert_quantity_news_json(self.news_quantity)
            try:
                self.log_label.destroy()
            except:
                pass
            self.log_error('Ready to run!', 0)
        except:
            self.window_settings.destroy()
            try:
                self.log_label.destroy()
            except:
                pass
            self.log_error('Value error in settings <News_Quantity> a default value was set <3>', 1)
            self.insert_quantity_news_json(3)
            self.news_quantity = 3
        if self.message == "":
            try:
                self.text_message.insert('1.0',"Custom message")
                self.insert_message_json('Custom message')
            except:
                pass
        self.window_settings.destroy()

    def get_news_globo(self):
        url = "https://g1.globo.com/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            eventos = soup.find_all(class_="bastian-feed-item")
            textos = []
            for evento in eventos:
                titulo_element = evento.find("a", class_="feed-post-link")
                if titulo_element:
                    texto = titulo_element.get_text().strip()
                    textos.append(texto)
            return textos
        else:
            return f"not found: {response.status_code}"

    def create_note(self):
        try:
            with open("data.txt", 'x') as file:
                pass
        except:
            pass
    
    def change_name_window(self):
        if len(self.Window_name.get()) <= 20:
            self.insert_name_window(self.Window_name.get())
            self.window_settings.destroy()
            try:
                self.log_label.destroy()
            except:
                pass
            self.log_error('Restart the program to set the new name', 0)
        else:
            self.window_settings.destroy()
            try:
                self.log_label.destroy()
            except:
                pass
            self.log_error('Error to set window name (max caractres/value = null)', 1)

    def get_name_window(self):
        name = self.read_json()['window_name']
        if name == "":
            name = "Automated - OBS"
        return name

    def insert_note(self):
        try:
            self.start_btn.destroy()
            self.running_button()
            t = self.read_json()['quantity_news']
            m = self.read_json()['message']
            note = 0
            insert_note_count = 0
            #print(len(self.get_news_globo()))
            
            with open('data.txt', 'w', encoding="utf-8") as file:
                while note != len(self.get_news_globo()):
                    if insert_note_count == t:
                        file.write(f"{m} - ")
                        insert_note_count = 0
                    else:
                        file.write(f"{self.get_news_globo()[note]} - ")
                        insert_note_count += 1
                    note += 1
            try:
                self.log_label.destroy()
            except:
                pass
            self.log_error('Open Text (GDI+) in obs Studio and select data.txt', 0)
            self.running_btn.destroy()
            self.start_button()
        except:
            try:
                self.log_label.destroy()
            except:
                pass
            self.log_error('Error: verify functions using Web Scraping', 1)
            self.running_btn.destroy()
            self.start_button()

if __name__ == "__main__":
    s = Software()
    s.window.mainloop()