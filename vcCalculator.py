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

        if data.find('ouvre') >= 0 and data.find('youtube') >= 0:
            print("J ouvre youtube")
            self.start.action("youtube")
        
        if data.find('ouvre') >= 0 and data.find('spotify') >= 0:
            print("J ouvre spotify")
            self.start.action("spotify")

        if data.find("quel") >= 0 and data.find('temps') >= 0:
            print("Voila la meteo")
            self.start.action("meteo")

        if data.find('clear') >= 0:
            self.start.action('clear')
