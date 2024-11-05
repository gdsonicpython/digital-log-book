import json
import sys
from modules import *
from cryptography.fernet import Fernet
from datetime import datetime

def create_log(person:str, log:str):
    key = Fernet.generate_key()
    enclog = Fernet(key).encrypt(log.encode())
    finlog = {"user":person, "log":str(enclog)[2:][:-1], "time":str(datetime.now())}
    return finlog, str(key)[2:][:-1]

def addlog(logdata, keydata, person:str, log:str):
    log,key = create_log(person, log)

    logdata.append(log)
    keydata.append(key)
    return logdata, keydata

def writelogs(logdata, keydata):
    with open("keys.json", "w") as file:
        file.write(json.dumps(keydata))

    with open("logs.json", "w") as file:
        file.write(json.dumps(logdata))



CURRENT_MESSAGE = ""

with open("keys.json") as file:
    keydata = json.loads(file.read())

with open("logs.json") as file:
    logdata = json.loads(file.read())

while True:
    rlw = select_option_add(["write a log", "read a log", "save and exit", "save", "exit"], CURRENT_MESSAGE)
    if rlw == 0:
        username = input("put in your name > ")
        log = input("put in your log > ")
        logdata, keydata = addlog(logdata, keydata, username, log)
        CURRENT_MESSAGE = "log made by " + username + " was added"
    elif rlw == 1:
        logs = []
        n = 1
        for i in range(len(logdata)):
            logs.append(str(i+1) + ". Log made by " + logdata[i]["user"] + " at " + logdata[i]["time"])
        
        log_index = select_option(logs+["exit"])
        if log_index != len(logs):
            log_options = select_option(["read log", "erase log"])
            if log_options == 0:
                dec = Fernet(keydata[log_index].encode()).decrypt(logdata[log_index]["log"].encode())
                select_option([dec.decode()])
            elif log_options == 1:
                eraseornot = select_option_add(["yes", "no"], "are you sure you want to delete this log")
                if eraseornot == 0:
                    del logdata[log_index]
                    del keydata[log_index]
                elif eraseornot == 1:
                    CURRENT_MESSAGE = "log has not been deleted"
    elif rlw == 2:
        writelogs(logdata, keydata)
        sys.exit()
    elif rlw == 3:
        writelogs(logdata, keydata)
        select_option(["saved logs..."])
    elif rlw == 4:
        a = select_option_add(["yes", "no"], "are you sure you want to exit without saving")
        if a == 0:
            sys.exit()