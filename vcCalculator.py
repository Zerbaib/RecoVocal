from executeur import start

class interpreter(start):
    def __init__(self):
        super().__init__()
        self.start = start()
        self.status = 1

    def interpret(self, data):
        data = data
        #print(data.find('framboises'))
        if data.find('bonjour') >= 0:
            print("Bonjour !")
            print("Que pui-je faire pour toi ?")

        if data.find("ouvre") >= 0 and data.find("discord") >= 0:
            print("J ouvre Discord")
            self.start.action("discord")

        if data.find('allume') >= 0 and data.find('rouge') >= 0:
            print("J allume la rouge")
            self.start.action("red on")

