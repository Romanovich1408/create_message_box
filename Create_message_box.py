class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
    
    def __str__(self):
        return 'Message [sender = '+str(self.sender+' , text = '+str(self.text)+']')

class MessageBox:
    def __init__(self):
        self.messages = []
    
    def add_message (self, message):
        self.messages.append(message)

    def get_last_message(self):
        if len(self.messages) == 0:
            return None
        else:
            message = self.messages[-1]
            return message
    
    def __str__(self):
        result = ''
        for message in self.messages:
            result+=str(message)+''
        return result



message_box_1 = MessageBox()



message_1 = Message('Maxim', 'Hello')
message_2 = Message('Inna', 'Love you')

message_box_1.add_message(message_1)
message_box_1.add_message(message_2)

print(message_box_1)

message_3 = message_box_1.get_last_message()

print(message_3)






