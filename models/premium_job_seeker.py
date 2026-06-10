#Inheriting from Job seeker class
from models.job_seeker import JobSeeker
#Defing the class
class PremiumJobSeeker(JobSeeker):
    #Defing the init contructor with addition membership type
    def __init__(self, name, email, skills, membership_type):
        super().__init__(name, email, skills)
        self.membership_type = membership_type
    #Defining function priority
    def priority_apply(self):
        print("Priority application enabled")