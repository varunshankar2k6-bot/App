class User:

    total_users = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users += 1

    def display_details(self):
        print("Name:", self.name)
        print("Email:", self.email)

    @staticmethod
    def validate_email(email):
        return "@" in email

    @classmethod
    def get_total_users(cls):
        return cls.total_users