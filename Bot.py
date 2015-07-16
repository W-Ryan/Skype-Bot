#Skype4Py does not work with the new cloud chats.
import Skype4Py

prefix = "S Bot> "

def send(chat, msg):
    Chat.SendMessage(prefix+msg)

def command(chat, status):
    if status == 'SENT' or status == 'RECEIVED':
        msg = Message.Body.lower()
        sender = Message.FromDisplayName
        skypeId = Message.FromHandle
        if (msg.startswith(',help')):
            send(chat, "I am S Bot. You can view by Github repo here: ")
            send(chat, "https://github.com/W-Ryan/Skype-Bot/")
        
skype = Skype4Py.Skype()
skype.OnMessageStatus = command
skype.Attach()

while True:
    try:
        raw_input('')
    except(Exception):
        raw_input('')
