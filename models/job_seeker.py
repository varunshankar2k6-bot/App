#Inheriting from class user and logger 
from models.user import User
from utils.decorators import logger
#Defing class
class JobSeeker(User):
    #Basic init constructor function
    def __init__(self, name, email, skills):
        super().__init__(name, email)
        self.skills = skills
    #Applying the logger function
    @logger
    def apply_job(self, job_title):
        print(self.name, "applied for the position ", job_title)