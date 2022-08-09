import base64
import os

x = "C:\\Users\\abdul\\Desktop\\Abdullah\\Python Projeleri\\Key logger"
dl = os.listdir(x)
dl.remove("main.py")
dl.remove(".idea")
print(dl)

def encodes():
    i = 0
    while i < len(dl):
        with open(dl[i], "r", encoding="ansi") as file:
            a = file.read()
            message_bytes = a.encode('ansi')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ansi')
            with open(dl[i], "w", encoding="ansi") as f:
                f.write(str(base64_message))
        i += 1

def decodes():
    i = 0
    while i < len(dl):
        with open(dl[i], "r", encoding="ansi") as file:
            a = file.read()
            base64_bytes = a.encode('ansi')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ansi')
            with open(dl[i], "w", encoding="ansi") as f:
                f.write(str(message))

        i += 1


decodes()