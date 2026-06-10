#Qn 7 overloading class 
#Creating JobApplication class
class JobApplication:
    def __init__(self, applicant_name, experience):
        self.applicant_name = applicant_name
        self.experience = experience
    #Overloading uing gt 
    def __gt__(self, other):
        return self.experience > other.experience