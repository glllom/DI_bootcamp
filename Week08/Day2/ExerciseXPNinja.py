class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, another_phone):
        action = f"{self.phone_number} called to {another_phone.phone_number}."
        print(action)
        self.call_history.append(action)

    def send_message(self, another_phone, message):
        action = f"{self.phone_number} sent message to {another_phone.phone_number} with text: {message}."
        print(action)
        self.messages.append({"to": another_phone.phone_number, "from": self.phone_number, "content": message})
        another_phone.messages.append({"to": self.phone_number, "from": another_phone.phone_number, "content": message})

    def show_call_history(self):
        print(*self.call_history, sep='\n')

    def show_outgoing_messages(self):
        print(*iter(self.messages))

    def show_incoming_messages(self):
        pass

    def show_messages_from(self, another_phone):
        pass


p1 = Phone("123")
p2 = Phone("456")
p3 = Phone("789")

p1.call(p2)
p2.send_message(p1, "hello")
p1.send_message(p3, "whats up?")
p3.send_message(p1, "Fine")
p3.send_message(p2, "good morning")
p2.send_message(p3, "hi!")


p1.show_outgoing_messages()
