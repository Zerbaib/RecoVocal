import os

class start:
    def action(self, data):
        data = data
        if data == "discord":
            os.system(r"start C:\Users\nikam\AppData\Local\Discord\app-1.0.9007\Discord.exe")
            print()
        if data == "youtube":
            os.system("start https://youtube.com")
            print()
            #gp.output(16, gp.LOW)
        if data == "meteo":
            os.system("start https://search.brave.com/search?q=meteo&source=desktop")
            print()
            #gp.output(20, gp.HIGH)
        if data == "clear":
            os.system("cls")
            print()
            #gp.output(20, gp.LOW)
        if data == "spotify":
            os.system("start spotify")
            print()
            #gp.output(21, gp.HIGH)
        if data == "blue off":
            print()
            #gp.output(21, gp.LOW)