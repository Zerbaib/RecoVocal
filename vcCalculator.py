from executeur import start

class interpreter(start):
    def __init__(self):
        super().__init__()
        self.start = start()
        self.status = 1

    def interpret(self, data):
        data = data
        #print(data.find('framboises'))
        if data.find('framboises') >= 0:
            print("Oui")
        if data.find('allume') >= 0 and data.find('rouge') >= 0:
            print("J allume la rouge")
            self.start.action("red on")
        if data.find('eteint') >= 0 and data.find('rouge') >= 0:
            print("J eteint la rouge")
            self.start.action("red off")
        if data.find('allume') >= 0 and data.find('verte') >= 0:
            print("J allume la verte")
            self.start.action("green on")
        if data.find('eteint') >= 0 and data.find('verte') >= 0:
            print("J eteint la verte")
            self.start.action("green off")
        if data.find('allume') >= 0 and data.find('bleu') >= 0:
            print("J allume la bleu")
            self.start.action("blue on")
        if data.find('eteint') >= 0 and data.find('bleu') >= 0:
            print("J eteint la bleu")
            self.start.action("blue off")
