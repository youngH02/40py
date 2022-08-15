import threading
from playsound import playsound

def loopSound():
    while True:
        playsound('audio.mp3', block=True)

# providing a name for the thread improves usefulness of error messages.
loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True # shut down music thread when the rest of the program exits
loopThread.start()

while True:
    raw_input("Put your gameplay loop here.")