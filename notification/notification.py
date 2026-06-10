#Defining new class Notification
class Notification:
    def send(self):
        pass
#Defining various methods inside the class as seperate classes
class EmailNotification(Notification):
    def send(self):
        print("Email Notification Sent")
class SMSNotification(Notification):
    def send(self):
        print("SMS Notification Sent")
class WhatsAppNotification(Notification):
    def send(self):
        print("WhatsApp Notification Sent")