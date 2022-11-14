import os

class start:
    def action(self, data):
        data = data
        if data == "discord":
            os.system(r"C:\Users\nikam\AppData\Local\Discord\Update.exe")
            print()
        if data == "red off":
            print()
            #gp.output(16, gp.LOW)
        if data == "green on":
            print()
            #gp.output(20, gp.HIGH)
        if data == "green off":
            print()
            #gp.output(20, gp.LOW)
        if data == "blue on":
            print()
            #gp.output(21, gp.HIGH)
        if data == "blue off":
            print()
            #gp.output(21, gp.LOW)