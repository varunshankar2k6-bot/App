#Defining class User
class User:
    #Initializing as 0 at beginning
    total_users = 0
    #Defining basic method constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users += 1
    #Defing display details method
    def display_details(self):
        print("Name:", self.name)
        print("Email:", self.email)
    #Static method to check if email is valid or not
    @staticmethod
    def validate_email(email):
        return "@" in email
    #Class method to get total users
    @classmethod
    def get_total_users(cls):
        return cls.total_users