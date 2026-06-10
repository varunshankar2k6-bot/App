#Qn 10 Creating Singleton Pattern
class Database:
    _instance = None
    def __new__(cls):
        #To check instance for singleton
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance