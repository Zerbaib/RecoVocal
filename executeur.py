import os

class start:
    def action(self, data):
        data = data
        if data == "blue off":
            print()
        elif data == "clear":
            os.system("cls")
            print()
        elif data == "discord":
            os.system(r"start C:\Users\nikam\AppData\Local\Discord\app-1.0.9007\Discord.exe")
            print()
        elif data == "meteo":
            os.system("start https://search.brave.com/search?q=meteo&source=desktop")
            print()
        elif data == "spotify":
            os.system("start spotify")
            print()
        elif data == "youtube":
            os.system("start https://youtube.com")
            print()
            #gp.output(21, gp.LOW)