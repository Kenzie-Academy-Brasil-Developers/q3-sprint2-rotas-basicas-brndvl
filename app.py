from flask import Flask
from datetime import datetime, time

app = Flask(__name__)

now = datetime.now()

dict_home = {"data": "Hello Flask!"}

@app.route('/')
def home():
    return dict_home

dict_time = {"current_time": now}

@app.route('/current_datetime')
def data_time():
    time = now.strftime("%H")
    int_time = int(time)

    print(int_time)
    if int_time >= 0 and int_time <= 11:
        dict_time["message"] = "Bom dia!"
        return dict_time
    elif int_time >= 12 and int_time <= 17:
        dict_time["message"] = "Boa tarde!"
        return dict_time
    else:
        dict_time["message"] = "Boa noite!"
        return dict_time



